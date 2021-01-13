from all import get_variation_pct
from mocks import mock_MonetusFiaComposition


def test_get_variations():
    symbol = "IVVB11.SAO"
    res = get_variation_pct(symbol=symbol)
    assert symbol[:-4] in res
    assert res.get(symbol[:-4], "NotFound") != "NotFound"


def test_use_enum():
    mocked = mock_MonetusFiaComposition
    res = mocked.get_current_quotations()
    assert res
    assert res.get(mocked.BIDI11.name, "NotFound") != "NotFound"

def test_total_variation():
    all_variations = {'BIDI11':"22.21%",
                      'NTCO3':"4.62%",
                      'EZTC3':"5.53%",
                      'HAPV3':"17.68%",
                      'CVCB3':"-0.26%",
                      'UGPA3':"2.59%",
                      'MDIA3':"3.98%",
                      'HGTX3':"2.94%",
                      'RAPT4':"0.19%",
                      'GUAR3':"4.92%",
                      'GRND3':"5.84%",
                      'ABCB4':"-0.12%",
                      'POMO4':"7.02%",
                      'POMO3':"4.41%",
                      'CGRA3':"4.08%",}

    from get_variation_pct import calculate_variation_average
    assert calculate_variation_average(all_variations) == 8.134385000000002