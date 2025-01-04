wizard = "Wizard"
elf = "Elf"
human = "Human"
dragon = "Dragon"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

print("1) Wizard")
print("2) Elf")
print("3) Human")

character_choice = int(input("Choose your character: "))

while character_choice not in [1, 2, 3]:
    print("Invalid input. Please choose a valid character.")
    character_choice = int(input("Choose your character: "))


if character_choice == 1:
    print("You have chosen the character: Wizard")
    print("Health: 70")
    print("Damage: 150")
    character_name = wizard
    character_hp = wizard_hp
    character_damage = wizard_damage
    character_alias = input("Please give your character a name.").lower()
    print(f"Your character's name is: {character_alias}")

elif character_choice == 2:
    print("You have chosen the character: Elf")
    print("Health: 100")
    print("Damage: 100")
    character_name = elf
    character_hp = elf_hp
    character_damage = elf_damage
    character_alias = input("Please give your character a name.").lower()
    print(f"Your character's name is: {character_alias}")


elif character_choice == 3:
    print("You have chosen the character: Human")
    print("Health: 150")
    print("Damage: 20")
    character_name = human
    character_hp = human_hp
    character_damage = human_damage
    character_alias = input("Please give your character a name.").lower()
    print(f"Your character's name is: {character_alias}")


while character_hp > 0 and dragon_hp > 0:
    # Player's attack
    print(f"{character_alias} damages the Dragon!")
    dragon_hp -= character_damage
    print(f"The Dragon's hitpoints are now: {dragon_hp}")

    if dragon_hp <= 0:
        break

    # Dragon's counterattack
    print(f"The Dragon strikes back at the {character_alias}")
    character_hp -= dragon_damage
    print(f"The {character_alias}'s hitpoints are now: {character_hp}")

    if character_hp <= 0:
        break

# Check the outcome of the battle
if character_hp <= 0:
    print(f"The {character_name} has lost the battle.")
else:
    print("The Dragon has lost the battle.")
