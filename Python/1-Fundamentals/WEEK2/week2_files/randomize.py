import random


# simulates rolling a dice
pips = random.randint(1, 6)
print(f"You roll the die and it lands on: {pips}")

# like wheel of fortune
prizes = ["a car", "$10000", "a pony", "$500000"]
prize_won = random.choice(prizes)
print(f"You spin the wheel and you win: {prize_won}")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(f"The cards are now in this order: {cards}")
