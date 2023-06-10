from datetime import datetime

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class AccountHolder(User):
    def __init__(self, name, email, address, initial_deposit):
        super().__init__(name, email)
        self.address = address
        self.__balance = initial_deposit
        self.__loaned = 0
        self.__transaction_history = []

    @property
    def balance(self):
        return self.__balance

    @property
    def loaned(self):
        return self.__loaned

    def deposit(self, amount):
        self.__balance += amount
        self.record_transaction("Deposit", amount)

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            self.record_transaction("Withdrawal", amount)
        else:
            print("the bank is bankrupt")

    def check_balance(self):
        print(f"{self.name} Balance: {self.__balance}")

    def transfer_balance(self, amount, recipient):
        if self.__balance >= amount:
            self.__balance -= amount
            recipient.__balance += amount
            self.record_transaction("Transfer", amount)
            recipient.record_transaction("Received", amount)
            print("Balance transferred successfully")
        else:
            print("Insufficient balance")

    def take_loan(self, amount, bank):
        if bank.get_loan_application_status():
            if self.__loaned == 0 and amount <= 2 * self.__balance:
                self.__loaned = 2 * self.__balance
                self.record_transaction("Loan", 2 * self.__balance)
                print(f"BDT {2 * self.__balance}/- added to account as loan")
            else:
                print(
                    f"You can't request a loan more than {2 * self.__balance}\-. Request Denied"
                )
        else:
            print(
                f"Dear {self.name}, loan applications are not being accepted. Sorry for the inconvenience"
            )

    def record_transaction(self, tr_type, amount):
        transaction = {
            "type": tr_type,
            "amount": amount,
            "time": datetime.now().strftime("%H:%M:%S"),
        }
        self.__transaction_history.append(transaction)

    def transaction_history(self):
        print(f"{self.name} transaction details are:\n")
        for transaction in self.__transaction_history:
            tr = f"Type: {transaction['type']}, Amount: {transaction['amount']}, Time: {transaction['time']}\n"
            print(tr)

    def __repr__(self):
        acc_holder_details = f"Name: {self.name}\n"
        acc_holder_details += (
            f"Balance: {self.__balance}\n----------------------------\n"
        )
        return acc_holder_details


class Admin(User):
    def __init__(self, name, email, password):
        super().__init__(name, email)
        self.password = password

    def create_new_account(self, account, bank):
        bank.create_new_account(account)

    def total_bank_balance(self, bank):
        return bank.total_bank_balance()

    def total_loan_given(self, bank):
        return bank.total_loan_given()

    def toggle_loan_on_off(self, bank, password):
        bank.toggle_loan_on_off(password)
