import random

high_score = 0


def dice_game():

    # make sure high_score is usable in the game
    global high_score

    while True:
        print(f"""
          Current High Score: {high_score}
            1. Roll Dice
            2. Leave Game
          Enter your choice: """)

        choice = input()

        # Input validation: only allow choices 1 or 2
        if not choice.isdigit() or int(choice) not in [1, 2]:
            print("Please enter 1 to roll the dice or 2 to leave the game.")
            continue

        choice_int = int(choice)

        if choice_int == 1:

            dice_one = random.randint(1, 6)
            dice_two = random.randint(1, 6)

            print(f"You roll a... {dice_one}")
            print(f"You roll a... {dice_two}")

            total_score = dice_one + dice_two
            print(f"You have rolled a total score of: {total_score}")

            if total_score > high_score:
                high_score = total_score
                print(f"New high score! Your new high score is: {high_score}")

        elif choice_int == 2:

            print(f"Goodbye!")
            break


dice_game()
