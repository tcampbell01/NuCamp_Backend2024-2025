def login(database, username, password):

    for db_username, db_password in database.items():
        if db_username == username and db_password == password:
            print(f"""Welcome, {username}!""")
            return username
        elif db_username == username and db_password != password:
            print(f"""Your password isn't correct""")
            return ""
        else:
            print("Your username was not found. Please register. ")
            return ""


def register(database, username):
    for db_username in database.items():
        if db_username == username:
            print("Username already registered")
            return ""
        else:
            print(f"""{username} has been registered""")
            return username
