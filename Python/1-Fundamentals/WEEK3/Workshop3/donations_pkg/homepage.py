def show_homepage():
    print("""
                === DonateMe Homepage ===
     ----------------------------------------------------
    |  1.   Login            |   2.  Register            |
     ----------------------------------------------------
    |  3.   Donate           |   4.  Show Donations      |
     ----------------------------------------------------
    |                   5.  Exit                         |
     ----------------------------------------------------    
    """)


def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = (f"""{username} donated ${donation_amt}.""")
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations):
    print("\n---All Donations---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donation_string in donations:
            print(donation_string)
