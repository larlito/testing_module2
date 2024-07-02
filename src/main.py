def average(lst):
    if not lst:
        raise ValueError("List is empty")
    return sum(lst) / len(lst)


class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


class User:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.count += 2

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def up_age(self):
        self.age += 0
        return self.age
