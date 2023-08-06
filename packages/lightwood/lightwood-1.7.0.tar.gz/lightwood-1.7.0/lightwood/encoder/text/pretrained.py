"""
2021.07.16
Adding flag "embedmode".

Embed-mode is made for when text is one of many columns in the model.
IF the model is direct (text) -> output, then it's worth just using
the fine-tuned encoder as the "mixer" persay; thus, turn embed-mode OFF.

This means there are 3 possible modes:

(1) Classification
    -> Fine tuned, output of encoder is [CLS] embedding
    -> Fine tuned, output of encoder is the class value
(2) Regression
    -> Untrained; output of encoder is [CLS] embedding

Training with regression is WIP; seems like quantile-binning is the best approach
but using MSE loss while fine-tuning did not demonstrate decent results. Particularly
because the mixer seems to address this.

2021.03.18

## Padding changes the answer slightly in the model.

The following text encoder uses huggingface's
Distilbert. Internal benchmarks suggest
1 epoch of fine tuning is ideal [classification].
Training ONLY occurs for classification. Regression problems
are not trained, embeddings are directly generated.

See: https://huggingface.co/transformers/training.html
for further details.

Currently the model supports only distilbert.

When instantiating the DistilBertForSeq.Class object,
num_labels indicates whether you use classification or regression.

See: https://huggingface.co/transformers/model_doc/distilbert.html#distilbertforsequenceclassification
under the 'labels' command

For classification - we use num_labels = 1 + num_classes ***

If you do num_classes + 1, we reserve the LAST label
as the "unknown" label; this is different from the original
distilbert model. (prior to 2021.03)

TODOs:
+ Regression
+ Batch encodes() tokenization step
+ Look into auto-encoding lower dimensional representations
of the output embedding
+ Look into regression tuning (will require grad. clipping)
+ Look into tuning to the encoded space of output.
"""
import time
import torch
from torch.utils.data import DataLoader
import os
import pandas as pd
from lightwood.encoder.text.helpers.pretrained_helpers import TextEmbed
from lightwood.helpers.device import get_devices
from lightwood.encoder.base import BaseEncoder
from lightwood.helpers.log import log
from lightwood.helpers.torch import LightwoodAutocast
from lightwood.api import dtype
from transformers import (
    DistilBertModel,
    DistilBertForSequenceClassification,
    DistilBertTokenizerFast,
    AdamW,
    get_linear_schedule_with_warmup,
)
from lightwood.helpers.general import is_none


class PretrainedLangEncoder(BaseEncoder):
    is_trainable_encoder: bool = True

    """
    Pretrained language models.
    Option to train on a target encoding of choice.

    Args:
    is_target ::Bool; data column is the target of ML.
    model_name ::str; name of pre-trained model
    custom_tokenizer ::function; custom tokenizing function
    batch_size  ::int; size of batch
    max_position_embeddings ::int; max sequence length of input text
    custom_train ::Bool; If true, trains model on target procided
    frozen ::Bool; If true, freezes transformer layers during training.
    epochs ::int; number of epochs to train model with
    embed_mode ::Bool; If true, assumes the output of the encode() step is the CLS embedding.
    """

    def __init__(
        self,
        stop_after: float,
        is_target=False,
        model_name="distilbert",
        custom_tokenizer=None,
        batch_size=10,
        max_position_embeddings=None,
        frozen=False,
        epochs=1,
        output_type=None,
        embed_mode=True,
    ):
        super().__init__(is_target)

        self.output_type = output_type
        self.name = model_name + " text encoder"
        log.info(self.name)

        self._max_len = max_position_embeddings
        self._frozen = frozen
        self._batch_size = batch_size
        self._epochs = epochs

        # Model setup
        self._tokenizer = custom_tokenizer
        self._model = None
        self.model_type = None

        # TODO: Other LMs; Distilbert is a good balance of speed/performance
        self._classifier_model_class = DistilBertForSequenceClassification
        self._embeddings_model_class = DistilBertModel
        self._tokenizer_class = DistilBertTokenizerFast
        self._pretrained_model_name = "distilbert-base-uncased"

        self.device, _ = get_devices()
        self.stop_after = stop_after

        self.embed_mode = embed_mode
        self.uses_target = True
        self.output_size = None

        # DEBUGGING!!!
        if self.embed_mode:
            log.info("Embedding mode on. [CLS] embedding dim output of encode()")
        else:
            log.info("Embedding mode off. Logits are output of encode()")

    def prepare(self, train_priming_data: pd.Series, dev_priming_data: pd.Series, encoded_target_values: torch.Tensor):
        """
        Prepare the encoder by training on the target.

        Training data must be a dict with "targets" avail.
        Automatically assumes this.
        """
        os.environ['TOKENIZERS_PARALLELISM'] = 'true'
        priming_data = pd.concat([train_priming_data, dev_priming_data])
        priming_data = priming_data.values
        if self.is_prepared:
            raise Exception("Encoder is already prepared.")

        # TODO: Make tokenizer custom with partial function; feed custom->model
        if self._tokenizer is None:
            self._tokenizer = self._tokenizer_class.from_pretrained(self._pretrained_model_name)

        # Replaces empty strings with ''
        priming_data = [x if x is not None else "" for x in priming_data]

        # Checks training data details
        # TODO: Regression flag; currently training supported for categorical only

        if (self.output_type in (dtype.categorical, dtype.binary)):
            log.info("Training model.")

            # Prepare priming data into tokenized form + attention masks
            text = self._tokenizer(priming_data, truncation=True, padding=True)

            log.info("\tOutput trained is categorical")

            labels = encoded_target_values.argmax(dim=1)

            # Construct the model
            self._model = self._classifier_model_class.from_pretrained(
                self._pretrained_model_name,
                num_labels=len(encoded_target_values[0]),
            ).to(self.device)

            # Construct the dataset for training
            xinp = TextEmbed(text, labels)
            dataset = DataLoader(xinp, batch_size=self._batch_size, shuffle=True)

            # If max length not set, adjust
            if self._max_len is None:
                self._max_len = self._model.config.max_position_embeddings

            if self._frozen:
                log.info("\tFrozen Model + Training Classifier Layers")
                """
                Freeze the base transformer model and train
                a linear layer on top
                """
                # Freeze all the transformer parameters
                for param in self._model.base_model.parameters():
                    param.requires_grad = False

                optimizer_grouped_parameters = self._model.parameters()

            else:
                log.info("\tFine-tuning model")
                """
                Fine-tuning parameters with weight decay
                """
                no_decay = [
                    "bias",
                    "LayerNorm.weight",
                ]  # decay on all terms EXCLUDING bias/layernorms
                optimizer_grouped_parameters = [
                    {
                        "params": [
                            p
                            for n, p in self._model.named_parameters()
                            if not any(nd in n for nd in no_decay)
                        ],
                        "weight_decay": 0.01,
                    },
                    {
                        "params": [
                            p
                            for n, p in self._model.named_parameters()
                            if any(nd in n for nd in no_decay)
                        ],
                        "weight_decay": 0.0,
                    },
                ]

            optimizer = AdamW(optimizer_grouped_parameters, lr=1e-5)
            scheduler = get_linear_schedule_with_warmup(
                optimizer,
                num_warmup_steps=0,  # default value for GLUE
                num_training_steps=len(dataset) * self._epochs,
            )

            # Train model; declare optimizer earlier if desired.
            self._tune_model(
                dataset, optim=optimizer, scheduler=scheduler, n_epochs=self._epochs
            )

        else:
            log.info("Target is not classification; Embeddings Generator only")

            self.model_type = "embeddings_generator"
            self._model = self._embeddings_model_class.from_pretrained(
                self._pretrained_model_name
            ).to(self.device)

            # TODO: Not a great flag
            # Currently, if the task is not classification, you must have
            # an embedding generator only.
            if self.embed_mode is False:
                log.info("Embedding mode must be ON for non-classification targets.")
                self.embed_mode = True

        self.is_prepared = True
        encoded = self.encode(priming_data[0:1])
        self.output_size = len(encoded[0])

    def _tune_model(self, dataset, optim, scheduler, n_epochs=1):
        """
        Given a model, train for n_epochs.
        Specifically intended for tuning; it does NOT use loss/
        stopping criterion.

        model - torch.nn model;
        dataset - torch.DataLoader; dataset to train
        device - torch.device; cuda/cpu
        log - lightwood.logger.log; log.info output
        optim - transformers.optimization.AdamW; optimizer
        scheduler - scheduling params
        n_epochs - number of epochs to train

        """
        self._model.train()

        if optim is None:
            log.info("No opt. provided, setting all params with AdamW.")
            optim = AdamW(self._model.parameters(), lr=5e-5)
        else:
            log.info("Optimizer provided")

        if scheduler is None:
            log.info("No scheduler provided.")
        else:
            log.info("Scheduler provided.")

        started = time.time()
        for epoch in range(n_epochs):
            total_loss = 0
            if time.time() - started > self.stop_after:
                break

            for batch in dataset:
                optim.zero_grad()

                with LightwoodAutocast():
                    inpids = batch["input_ids"].to(self.device)
                    attn = batch["attention_mask"].to(self.device)
                    labels = batch["labels"].to(self.device)
                    outputs = self._model(inpids, attention_mask=attn, labels=labels)
                    loss = outputs[0]

                total_loss += loss.item()

                loss.backward()
                optim.step()
                if scheduler is not None:
                    scheduler.step()

            self._train_callback(epoch, total_loss / len(dataset))

    def _train_callback(self, epoch, loss):
        log.info(f"{self.name} at epoch {epoch+1} and loss {loss}!")

    def encode(self, column_data):
        """
        TODO: Maybe batch the text up; may take too long
        Given column data, encode the dataset.

        Currently, returns the embedding of the pre-classifier layer.

        Args:
        column_data:: [list[str]] list of text data in str form

        Returns:
        encoded_representation:: [torch.Tensor] N_sentences x Nembed_dim
        """
        if self.is_prepared is False:
            raise Exception("You need to first prepare the encoder.")

        # Set model to testing/eval mode.
        self._model.eval()

        encoded_representation = []

        with torch.no_grad():
            # Set the weights; this is GPT-2
            for text in column_data:

                # Omit NaNs
                if is_none(text):
                    text = ""

                # Tokenize the text with the built-in tokenizer.
                inp = self._tokenizer.encode(
                    text, truncation=True, return_tensors="pt"
                ).to(self.device)

                if self.embed_mode:  # Embedding mode ON; return [CLS]
                    output = self._model.base_model(inp).last_hidden_state[:, 0]

                    # If the model has a pre-classifier layer, use this embedding.
                    if hasattr(self._model, "pre_classifier"):
                        output = self._model.pre_classifier(output)

                else:  # Embedding mode off; return classes
                    output = self._model(inp).logits

                encoded_representation.append(output.detach())

        return torch.stack(encoded_representation).squeeze(1).to('cpu')

    def decode(self, encoded_values_tensor, max_length=100):
        raise Exception("Decoder not implemented.")

    def to(self, device, available_devices):
        for v in vars(self):
            attr = getattr(self, v)
            if isinstance(attr, torch.nn.Module):
                attr.to(device)
        return self
