class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount} прошло успешно")
        else:
            raise ValueError("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Недостаточно средств на счету")
        elif amount <= 0:
            self.__balance -= amount
            raise ValueError("Сумма снятия должна быть положительной")
        else:
            self.__balance -= amount
            print(f"Снятие {amount} прошло успешно")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Начислены проценты: {interest}")


class CheckingAccount(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        else:
            self._BankAccount__balance -= amount
            print(f"Снятие {amount} прошло успешно, новый баланс: {self.get_balance()}")

savings = SavingsAccount("Alice", 500)
savings.deposit(500)
savings.withdraw(100)
savings.apply_interest()
print(f"Баланс сберегательного счёта: {savings.get_balance()}")

checking = CheckingAccount("Bob", 300)
checking.withdraw(400)
print(f"Баланс текущего счёта: {checking.get_balance()}")