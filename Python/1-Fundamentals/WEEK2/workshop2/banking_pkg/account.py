def show_balance(balance):
    print(f"""
          Your current balance is: ${balance}
          """
          )


def deposit(balance):
    while True:
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.  Please try again.")
                continue
            new_balance_after_deposit = balance + amount
            print(f"""
                  Deposited ${amount}. New balance is ${new_balance_after_deposit}
                  """)
            return new_balance_after_deposit
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def withdraw(balance):
    while True:
        try:
            withdrawl = int(input("Enter amount to withdraw: "))
            if withdrawl <= 0:
                print("Amount must be greater than zero. Try again.")
                continue
            if withdrawl > balance:
                print(f"""Insufficient funds!
                      You cannot withdraw more than your balance.
                      """)
                continue
            new_balance_after_withdrawl = balance - withdrawl
            print(f"""Withdrew ${withdrawl}.
                  New balance is ${new_balance_after_withdrawl}
                  """)
            return new_balance_after_withdrawl
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def logout(name):
    print(f"""
          Goodbye {name}!
          """
          )
