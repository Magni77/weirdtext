import pytest

from decoder import Decoder
from encoder import Encoder
from weird_text import WeirdText


@pytest.fixture
def encoder():
    return Encoder()


@pytest.fixture
def decoder():
    return Decoder()


@pytest.fixture
def weird_text(encoder, decoder):
    return WeirdText(encoder, decoder)
