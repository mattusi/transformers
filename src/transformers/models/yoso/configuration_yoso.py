# coding=utf-8
# Copyright 2022 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" YOSO model configuration"""

from ...utils.import_utils import register
from ...configuration_utils import PretrainedConfig
from ...utils import logging


logger = logging.get_logger(__name__)


from ..deprecated._archive_maps import YOSO_PRETRAINED_CONFIG_ARCHIVE_MAP  # noqa: F401, E402


@register()
class YosoConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`YosoModel`]. It is used to instantiate an YOSO
    model according to the specified arguments, defining the model architecture. Instantiating a configuration with the
    defaults will yield a similar configuration to that of the YOSO
    [uw-madison/yoso-4096](https://huggingface.co/uw-madison/yoso-4096) architecture.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 50265):
            Vocabulary size of the YOSO model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`YosoModel`].
        hidden_size (`int`, *optional*, defaults to 768):
            Dimension of the encoder layers and the pooler layer.
        num_hidden_layers (`int`, *optional*, defaults to 12):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 12):
            Number of attention heads for each attention layer in the Transformer encoder.
        intermediate_size (`int`, *optional*, defaults to 3072):
            Dimension of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
        hidden_act (`str` or `function`, *optional*, defaults to `"gelu"`):
            The non-linear activation function (function or string) in the encoder and pooler. If string, `"gelu"`,
            `"relu"`, `"selu"` and `"gelu_new"` are supported.
        hidden_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
        attention_probs_dropout_prob (`float`, *optional*, defaults to 0.1):
            The dropout ratio for the attention probabilities.
        max_position_embeddings (`int`, *optional*, defaults to 512):
            The maximum sequence length that this model might ever be used with. Typically set this to something large
            just in case (e.g., 512 or 1024 or 2048).
        type_vocab_size (`int`, *optional*, defaults to 2):
            The vocabulary size of the `token_type_ids` passed when calling [`YosoModel`].
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        layer_norm_eps (`float`, *optional*, defaults to 1e-12):
            The epsilon used by the layer normalization layers.
        position_embedding_type (`str`, *optional*, defaults to `"absolute"`):
            Type of position embedding. Choose one of `"absolute"`, `"relative_key"`, `"relative_key_query"`.
        use_expectation (`bool`, *optional*, defaults to `True`):
            Whether or not to use YOSO Expectation. Overrides any effect of num_hash.
        hash_code_len (`int`, *optional*, defaults to 9):
            The length of hashes generated by the hash functions.
        num_hash (`int`, *optional*, defaults to 64):
            Number of hash functions used in [`YosoSelfAttention`].
        conv_window (`int`, *optional*):
            Kernel size of depth-wise convolution.
        use_fast_hash (`bool`, *optional*, defaults to `False`):
            Whether or not to use custom cuda kernels which perform fast random projection via hadamard transform.
        lsh_backward (`bool`, *optional*, defaults to `True`):
            Whether or not to perform backpropagation using Locality Sensitive Hashing.

    Example:

    ```python
    >>> from transformers import YosoConfig, YosoModel

    >>> # Initializing a YOSO uw-madison/yoso-4096 style configuration
    >>> configuration = YosoConfig()

    >>> # Initializing a model (with random weights) from the uw-madison/yoso-4096 style configuration
    >>> model = YosoModel(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "yoso"

    def __init__(
        self,
        vocab_size=50265,
        hidden_size=768,
        num_hidden_layers=12,
        num_attention_heads=12,
        intermediate_size=3072,
        hidden_act="gelu",
        hidden_dropout_prob=0.1,
        attention_probs_dropout_prob=0.1,
        max_position_embeddings=4096,
        type_vocab_size=1,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        position_embedding_type="absolute",
        use_expectation=True,
        hash_code_len=9,
        num_hash=64,
        conv_window=None,
        use_fast_hash=True,
        lsh_backward=True,
        pad_token_id=1,
        bos_token_id=0,
        eos_token_id=2,
        **kwargs,
    ):
        super().__init__(pad_token_id=pad_token_id, bos_token_id=bos_token_id, eos_token_id=eos_token_id, **kwargs)

        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.intermediate_size = intermediate_size
        self.hidden_act = hidden_act
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.initializer_range = initializer_range
        self.type_vocab_size = type_vocab_size
        self.layer_norm_eps = layer_norm_eps
        self.position_embedding_type = position_embedding_type
        self.use_expectation = use_expectation
        self.hash_code_len = hash_code_len
        self.num_hash = num_hash
        self.conv_window = conv_window
        self.use_fast_hash = use_fast_hash
        self.lsh_backward = lsh_backward

__all__ = [
    "YosoConfig"
]
    