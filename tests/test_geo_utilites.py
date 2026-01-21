import pytest
from src.geo_utilities import rozpoznaj_uklad, strefa_2000


@pytest.mark.parametrize(
    "x,y,expected",
    [
        (356556.150000000023283, 528904.25, "2180"),
        (1516518987, 356556, None),
        (5661244.578599999658763, 7388427.696999999694526, "2178"),
    ],
)
def test_rozpoznaj(x, y, expected):
    assert rozpoznaj_uklad(x, y) == expected


@pytest.mark.parametrize(
    "y,strefa",
    [
        (5388427, "2176"),
        (6388427, "2177"),
        (7388427, "2178"),
        (8388427, "2179"),
        (9388427, None),
    ],
)
def test_strefa2000(y, strefa):
    assert strefa_2000(y) == strefa
