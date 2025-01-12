def login(database, username, password):

    if username in database and database[username] == password:
        print(f"""Welcome, {username}!""")
        return username
    elif username in database and database[username] != password:
        print(f"""Incorrect password for {username}""")
        return ""
    else:
        print("Your username was not found. Please register. ")
        return ""


def register(database, username, password):
    if username in database:
        print("Username already registered")
        return ""
    else:
        database[username] = password
        print(f"""Username '{username}' has been registered successfully!""")

        print("Current Database: ")
        print(database)

        return username
