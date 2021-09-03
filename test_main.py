import pytest
from main import suma


@pytest.mark.parametrize(
    "input_a, input_b, expected",
    [
        (3, 2, 5),
        (2, 3, 5),
        (suma(3, 2), 5, 10),
        (3, suma(2, 5), 10)
    ]
)
def test_suma_muti(input_a, input_b, expected):
    assert suma(input_a, input_b) == expected
