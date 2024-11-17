import pytest


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма депозита должна быть положительной!")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Недостаточно средств!")

    def get_balance(self):
        return self.__balance


class SavingAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        new_balance = self.get_balance() * (1 + self.interest_rate)
        self.deposit(new_balance - self.get_balance())


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        self.deposit(-amount)


def test_tinkoff_killer():
    saving_account = SavingAccount(owner="Denis", balance=0)

    saving_account.deposit(500)
    saving_account.withdraw(100)
    saving_account.apply_interest()

    assert saving_account.get_balance() > 0, "Баланс счета должен быть больше 0"
