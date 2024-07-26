import pytest
from src.generators import filter_by_currency,  transaction_descriptions

@pytest.mark.parametrize("n, expected",[])



def test_filter_by_currency(n, expected):
    assert filter_by_currency(n) == expected

def test_transaction_descriptions(n, expected):
    assert transaction_descriptions(n) == expected
