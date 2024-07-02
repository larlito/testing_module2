import pytest
from src.main import BankAccount

bank = BankAccount()
bank.deposit(1000)

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (100,1100),
                             (10000000000000,10000000001000)

                         ])

def test_bank_deposite_positive(value1,extend_result):
    bank.deposit(value1)
    assert bank.get_balance() == extend_result
    bank.withdraw(value1)


@pytest.mark.parametrize('value1, extend_result',
                         [
                             (-100,pytest.raises(ValueError)),
                             ('100', pytest.raises(TypeError)),
                             (0,pytest.raises(ValueError))
                         ])

def test_bank_deposite_negative(value1, extend_result):
    with extend_result:
        assert bank.deposit(value1) == extend_result



@pytest.mark.parametrize('value1,extend_result',
                         [
                             (100, 900),
                             (1000,0),
                         ])

def test_bank_withdraw_positive(value1, extend_result):
    bank.withdraw(value1)

    assert bank.get_balance() == extend_result
    bank.deposit(value1)

@pytest.mark.parametrize('value1,extend_result',
                         [
                             (1100, pytest.raises(ValueError)),
                         ])

def test_bank_withdraw_negative(value1,extend_result):
    with extend_result:
        assert bank.withdraw(value1) == extend_result








