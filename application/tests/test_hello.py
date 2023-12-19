import pytest

from application import hello


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Ed", "Hello Ed"),
    ],
)
def test_hello(name, expected):
    result = hello.hello(name=name)
    assert result == expected


def test_value_error():
    with pytest.raises(hello.NotAStringError):
        _ = hello.hello(name=1)
