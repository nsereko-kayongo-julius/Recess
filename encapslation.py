class BankAccount:
    def __init__(self, balance,  account_number):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds available")

    def get_balance(self):
        return self.__balance


# create a bank account
bank_account = BankAccount(1000, 12345)
print(bank_account.get_balance())
bank_account.deposit(500)
print(bank_account.get_balance())
bank_account.withdraw(100)
print(bank_account.get_balance())
