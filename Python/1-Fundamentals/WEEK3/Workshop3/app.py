from donations_pkg.homepage import show_homepage
from donations_pkg.user import login, register


database = {"admin": "password123"}

donations = []

authorized_user = ""

show_homepage()

if authorized_user == "":
    print("You must be logged into donate.")
else:
    print(f"""Logged in as: {authorized_user}""")


user_input = input("Choose number 1, 2, 3, 4, or 5:")

if user_input == "1":
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    authorized_user = login(database, username, password)

elif user_input == "2":
    username = input("Please enter your username: ")
    password = input("Please enter your password")

    authorized_user = register(database, username)

    if authorized_user != "":
        database[username] = password
elif user_input == "3":
    print("TODO: Write Donate Functionality")
elif user_input == "4":
    print("TODO: Write Show Donations Functionality")
else:
    print("Goodbye!")
