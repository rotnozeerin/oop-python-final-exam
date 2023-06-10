from bankmanagement import BankManagement
from user import AccountHolder, Admin


def main():
    pubali = BankManagement("Pubali")

    zeerin = AccountHolder("Zeerin", "zeerin@gmail.com", "Dhaka", 5000)
    orin = AccountHolder("Orin", "orin@gmail.com", "Dhaka", 5000)
    tarin = AccountHolder("Tarin", "tarin@gmail.com", "Dhaka", 5000)

    pubali.create_account(zeerin)
    pubali.create_account(orin)
    pubali.create_account(tarin)

    zeerin.deposit(5000)
    zeerin.check_balance()
    zeerin.transfer_balance(1500, orin)
    zeerin.check_balance()
    orin.check_balance()

    orin.take_loan(orin.balance, pubali)
    zeerin.transaction_history()
    orin.transaction_history()
    orin.withdraw(orin.balance)

    password = "admin123456"
    admin = Admin("admin", "admin12@gmail.com", password)
    pubali.admins[password] = admin
    pubali.toggle_loan_on_off(password)
    orin.take_loan(1500, pubali)

    print("\nAdmin access\n")
    pubali.toggle_loan_on_off(password)
    print("\n=====Current Bank State=======")
    print("Balance: ", end=" ")
    print(admin.total_bank_balance(pubali))
    print("Loan Given: ", end=" ")
    print(admin.total_loan_given(pubali))
    print("Net Balance: ", end=" ")
    print(pubali.net_balance())

    print("Admin access\n")
    print("======Account Details======")
    print(pubali)

if __name__ == "__main__":
    main()
