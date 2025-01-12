from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register


database = {"admin": "password123"}

donations = []

authorized_user = ""

show_homepage()

while True:
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

    user_input = input("Choose number 1, 2, 3, 4, or 5: ")

    if user_input == "1":
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        authorized_user = login(database, username, password)
        show_homepage()

    elif user_input == "2":
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")

        authorized_user = register(database, username, password)
        if authorized_user != "":
            show_homepage()

    elif user_input == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)
            show_homepage()

    elif user_input == "4":
        show_donations(donations)
        # Add the functionality to display donations if needed
        # For example: print(donations)

    elif user_input == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid input, please choose a valid option (1, 2, 3, 4, or 5).")
