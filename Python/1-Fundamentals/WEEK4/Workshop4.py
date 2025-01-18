class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name
        print("Your new name is: ", new_name)

    def change_pin(self, new_pin):
        self.pin = new_pin

        print("Your new pin is: ", new_pin)

    def change_password(self, new_password):
        self.password = new_password
        print("Your password has changed to: ", new_password)


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has an account balance of: ", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def transfer_money(self, recipient, amount):
        pin_identification = input("Enter your PIN: ")
        if pin_identification == self.pin:
            print("Transfer Authorized")
            self.balance = self.balance - amount
            recipient.balance = recipient.balance + amount

            print(f"{self.name} transferred ${amount} to {recipient.name}.")
            self.show_balance()
            recipient.show_balance()
            return True
        else:
            print("Incorrect PIN!")
            return False

    def request_money(self, sender, amount):
        print(f"You are requesting {amount} from {sender.name}")
        print("User authentication is required")
        sender_pin_identification = input(f"Enter {sender.name}'s PIN: ")
        if sender_pin_identification == sender.pin:
            password = input("Please enter your password: ")
            if password == self.password:
                print("Request authorized")
                sender.balance = sender.balance - amount
                self.balance = self.balance + amount
                print(f"{sender.name} sent {amount}")
                return True
            else:
                print("Invalid password. Transaction canceled.")
                return False
        else:
            print("Invalid PIN. Transaction canceled.")
            return False


"""Driver Code For Task 1"""

# user = User("Teresa", "2222", "Cold")
# print(user.name, user.pin, user.password)


# """Driver Code For Task 2"""
# user1 = User("Michael", "1234", "WestHartford")
# print("User: ", user1.name, "Pin: ", user1.pin, "Password: ", user1.password)

# user1.change_name("Erin")


# user1.change_pin("5555")


# user1.change_password("Minneapolis")

# print(user1.name, user1.pin, user1.password)

# """Driver Code For Task 3"""

# bank_user1 = BankUser("Teresa", "2222", "Cold")
# bank_user2 = BankUser("Michael", "3333", "Happy")
# print(f"{bank_user1.name}'s initial balance: ${bank_user1.balance}")
# bank_user1.deposit(2000)
# bank_user1.show_balance()
# bank_user1.withdraw(500)
# bank_user1.show_balance()

# """Driver Code For Task 4"""
# bank_user2.deposit(5000)
# bank_user2.show_balance()


"""Driver Code for Task 5"""

bank_user1 = BankUser("Teresa", "2222", "Cold")
bank_user2 = BankUser("Michael", "3333", "Happy")

bank_user2.deposit(5000)
bank_user2.show_balance()
bank_user1.show_balance()


if bank_user2.transfer_money(bank_user1, 500):

    print("Transfer successful!")

    bank_user2.request_money(bank_user1, 200)

    bank_user1.show_balance()
    bank_user2.show_balance()
