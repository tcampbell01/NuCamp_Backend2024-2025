import random


def guess_random_number(tries, start, stop):

    random_number = random.randint(start, stop)

    while tries > 0:
        guess = input("Please input a guess: ")
        if int(random_number) == int(guess):
            print("You guessed the number!")
            break
        elif int(random_number) > int(guess):
            print("Guess higher!")
        elif int(random_number) < int(guess):
            print("Guess lower!")

        tries -= 1

    if tries == 0:
        print(f"Sorry! You ran out of tries! The correct number was {random_number}")


# guess_random_number(5, 0, 10)


def guess_random_num_linear(tries, start, stop):
    
    
    random_number = random.randint(start, stop)
    
    
    
    
    for guess in range(start, stop + 1):
        print(f"Computer guesses: {guess}")
    
    
        if guess == random_number:
            print(f"Success! The correct number is {random_number}")
            return guess
        print("Not the correct number.  Trying again!")
        
        tries -= 1
        
        if tries == 0:
            print(f"Sorry, no more tries left. The correct number was {random_number}")
            return None
        
# guess_random_num_linear(5, 0, 10)
   
def guess_random_num_binary(tries, start, stop):
    
    
    random_number = random.randint(start, stop)
    # print(f"The random number is: {random_number}")
    
    lower_bound = start
    upper_bound = stop
    
    while tries > 0:
        pivot = (lower_bound + upper_bound) // 2
        # print(f"pivot is: {pivot}")
        

        if pivot == random_number:
            print(f"Success! The number was {random_number}")
            return pivot
        elif pivot > random_number:
            print(f"Guess lower!")
            upper_bound = pivot - 1
        else:
            print("Guess higher!")
            lower_bound = pivot + 1

        tries -= 1
        
        if tries == 0:
            print(f"Sorry, no more tries.  The number was {random_number}")
            return None

guess_random_num_binary(5, 0, 100)