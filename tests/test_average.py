import pytest
from src.main import average


@pytest.mark.parametrize('value1,extend_result',
                         [
                             ([1,2],1.5),
                             ([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30],15.5),
                             ([5,5],5),
                             ([-1,-2,-3],-2)
                         ])





def test_average_positive(value1,extend_result):
    assert average(value1) == extend_result


@pytest.mark.parametrize('value1,extend_result',
                         [
                             ([1,'2'],pytest.raises(TypeError)),
                             ('1,2',pytest.raises(TypeError)),
                             ([],pytest.raises(ValueError)),
                         ])


def test_average_negative(value1,extend_result):
    with extend_result:
        assert average(value1) == extend_result