transactions = [100, 50, -200, 457]

def count_balance(transactions):
    balance = 0
    for transaction in transactions:
        if transaction > 0:
            print(f'Пополнение на сумму {transaction}')
        else:
            print(f'Списание на сумму {transaction}')
        balance += transaction
    print(f"Финальный баланск: {balance}")

#count_balance(transactions)

def reach_min_balance(initial_balance, min_balance):
    while initial_balance < min_balance:
        print(f"Текущий баланс {initial_balance} меньше минимальной суммы. Добавляем депозит 100.")
        initial_balance += 100
    print(f"Достигнут минимальный баланс {min_balance}.")

#reach_min_balance(50, 300)

def check_transaction(transaction):
    if transaction > 0:
        print("Депозит")
    elif transaction < 0:
        print("Списание")
    else:
        print("Транзакция не меняет баланс")

# check_transaction(2400)
# check_transaction(-1000)
# check_transaction(0)


account_actions = {'initial_value': 100, "withdraw_1": -50, "withdraw_2": 50}
def print_action_names(account_actions):
    for action, value in account_actions.items():
        print(f"действия: {action}, значение: {value}")

# print_action_names(account_actions)


def safe_withdraw(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Сумма снятия больше доступного баланса")
        balance -= amount
        print(f"снятие произошло успешно, оставшийся баланс {balance}")
    except ValueError as error:
        print(error)

# safe_withdraw(1000, 4000)


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Депозит успешно добавлен")

# Создаем экземпляр класса Account
my_account = Account("Alice", 100)
print(f"Владелец: {my_account.owner}, Баланс: {my_account.balance}")

# Добавляем депозит
my_account.deposit(50)
print(f"Баланс после депозита: {my_account.balance}")