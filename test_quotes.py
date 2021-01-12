from all import get_quote_symbol
from mocks import mock_MonetusFiaComposition


def test_get_quotations():
    symbol = "IVVB11.SAO"
    res = get_quote_symbol(symbol=symbol)
    assert symbol[:-4] in res
    assert res.get(symbol[:-4], "NotFound") != "NotFound"


def test_use_enum():
    mocked = mock_MonetusFiaComposition
    res = mocked.get_current_quotations()
    assert res
    assert res.get(mocked.BIDI11.name, "NotFound") != "NotFound"
