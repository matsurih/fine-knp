import pytest

from fineknp import KNP


@pytest.fixture
def knp():
    return KNP()


def test_parse(knp: KNP):
    response = knp.parse('今日はいい天気だった')
    print(1)
    assert response == 1
