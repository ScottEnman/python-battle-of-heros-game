import random
import inquirer
from colorama import Fore, Style

# Define the character attributes.
class Character:
    def __init__(self, health, damage, agility):
        self.health = health
        self.damage = damage
        self.agility = agility

# Game introduction text
def introduction():
     print(f"{Fore.GREEN}Welcome to Battle of the Hero's.{Style.RESET_ALL}")
     print(f"{Fore.BLUE}Two players strategizing and battling to see who the true hero is!{Style.RESET_ALL}")

# Allows users to enter the player type they desire.
def player_selector(player):
    global health
    global type
    global selected_player

    # Provide player choice options for the user to select from the game terminal (local terminal).
    questions = [
    inquirer.List('players',
                    message="Select your player",
                    choices=['Wizard', 'Warrior', 'Healer'],
                ),
    ]

    selected_player = list(inquirer.prompt(questions).values())[0]

    print(f"{Fore.YELLOW}You have selected a {selected_player}.{Style.RESET_ALL}")
    print("")

    # Determine what player health and type is being used.
    if selected_player == "Wizard":
        health = wizard.health
        type = "Wizard"
    elif selected_player == "Warrior":
        health = warrior.health
        type = "Warrior"
    elif selected_player == "Healer":
        health = healer.health
        type = "Healer"

    return health, type, selected_player

# Defines what each dice roll attacks points are.
def attack(player, weapon_multiplier):
    global health
    dice_values = [1, 2, 3, 4, 5, 6]

    # Rolling the dice: Randomly select a dice roll value
    roll_value = random.choice(dice_values)
    print(f"{Fore.RED}The dice roll is {roll_value}{Style.RESET_ALL}")

    # Define what each dice roll value is.
    if roll_value == 1:
            health = 5
    elif roll_value == 2:
            health = 10
    elif roll_value == 3:
            health = 15
    elif roll_value == 4:
            health = 20
    elif roll_value == 5:
            health = 25
    elif roll_value == 6:
            health = 30

    print(f"{player}: {Fore.YELLOW}loses {health * weapon_multiplier} health points.{Style.RESET_ALL}")

# NOT USED YET: Define how to calculate whether the defense move is an attack or defense and what the health point value will be.
def defense_move():
    global special_defense
    global defense_value

    # Calculate the 'special_defense' type to be used.
    special_defense_choice = ["defend", "attack"]
    special_defense = random.choice(special_defense_choice)

    # Calculate the 'defense_value' to be used.
    if special_defense == "defend":
        defend = [5, 20, 20, 20, 25, 25, 25, 40]
        defense_value = random.choice(defend)
        print(f"Special Move Activated: Defense will be applied against upcoming attack by adding {defense_value} health points to defending player.")
    else:
        attack = [5, 20, 20, 20, 25, 25, 25, 40]
        defense_value = random.choice(attack)
        print(f"Special Move Activated: Attack will be applied against upcoming attack by removing {defense_value} health points from attacking player.")

    return special_defense, defense_value

# Randomly selects which player plays first.
def first_to_play():
    global player_1
    global player_2

    name_one = input(f"{Fore.GREEN}Enter a player name: {Style.RESET_ALL}")
    name_two = input(f"{Fore.GREEN}Enter another player name: {Style.RESET_ALL}")

    # Set values for player 1 and 2 to be used in a random selection to determine who plays first.
    name_values = [1, 2]

    # Randomly select who plays first.
    first_player = random.choice(name_values)

    if first_player is name_values[0]:   
        print(f"{Fore.YELLOW}Player 1: {name_one} selects their character and plays first.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Player 2: {name_two} selects their character and plays second.{Style.RESET_ALL}")
        print("----------------------------------------------")
        print("")
        player_1 = name_one
        player_2 = name_two

        return player_1, player_2
    else:
        print(f"{Fore.YELLOW}Player 1: {name_two} selects their character and plays first.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Player 2: {name_one} selects their character and plays second.{Style.RESET_ALL}")
        print("----------------------------------------------")
        print("")    
        player_1 = name_two
        player_2 = name_one

        return player_1, player_2

# Player selects attack_type to determine what multiplier is applied to the health points that are lost.
def attack_choice(player, type):
    global weapon_multiplier
    global weapons

    # Randomly apply an attack multiplier that will be multiplied against the dice roll value to determine how many health poiints the player loses.
    attack_values = [2,3]
    attack_value = random.choice(attack_values)

    # Provide weapon choice options for each player 'type' to select from the game terminal (local terminal).
    if type == "Wizard":
        questions = [
        inquirer.List('weapons',
                        message="Pick your attack spell",
                        choices=['Fire', 'Wind', 'Earth', 'Water'],
                    ),
        ]

        weapons = list(inquirer.prompt(questions).values())[0]
    elif type == "Warrior":
        questions = [
        inquirer.List('weapons',
                        message="Pick your attack weapon",
                        choices=['Longbow', 'Sword', 'Axe', 'Spear'],
                    ),
        ]

        weapons = list(inquirer.prompt(questions).values())[0]

    elif type == "Healer":
        questions = [
        inquirer.List('weapons',
                        message="Pick your attack type",
                        choices=['Force Field', 'Enchanted Dagger', 'Staff','Crossbow'],
                    ),
        ]

        weapons = list(inquirer.prompt(questions).values())[0]

    weapon_multiplier = attack_value
    return weapon_multiplier

# ONLY HEALTH USED CURRENTLY: Character attributed (Health, Damage, Agility).
wizard = Character(150, 100, 100)
warrior = Character(150, 100, 100)
healer = Character(150, 100, 100)

# Execute the game's introduction
introduction()

# Execute who plays first.
first_to_play()

# Set player variables
player_one = player_selector(player_1)
player_one_type = type
player_one_turns = 1
player_one_health = health

player_two = player_selector(player_2)
player_two_type = type
player_two_turns = 1
player_two_health = health

# Describe each player
print(f"{player_1}: {Fore.GREEN}{player_one_type} has a starting health of {player_one_health}.{Style.RESET_ALL}")
print(f"{player_2}: {Fore.GREEN}{player_two_type} has a starting health of {player_two_health}.{Style.RESET_ALL}")
print("----------------------------------------------")
print("")

# GAME PLAY: Attack until one player loses all of their health points.
while health > 0:

    # PLAYER 1's turn to play:
    print(f"{player_1}: {Fore.YELLOW}ATTACK{Style.RESET_ALL}")

    attack_choice(player_1, player_one_type)
    attack(player_2, weapon_multiplier)

    # Calculate player 2's remaining health points.
    player_two_health = player_two_health - (health * weapon_multiplier)

    print(f"{player_2}: {Fore.GREEN}{player_two_type} has {player_two_health} health points left.{Style.RESET_ALL}")
    print(f"{player_1}: {Fore.YELLOW}took {player_one_turns} turn(s) so far.{Style.RESET_ALL}")
    print("----------------------------------------------")
    print("")

    # Increment player 1 turns count.
    player_one_turns += 1

    # Finish the game if player 2's health falls below 0.
    if player_two_health <= 0:
        print(f"{player_1}: {Fore.GREEN}WINS with {player_one_health} points!!{Style.RESET_ALL} {player_2}: {Fore.RED}LOSES with {player_two_health} points!!{Style.RESET_ALL}")
        exit(0)

    # PLAYER 2's turn to play:
    print(f"{player_2}: {Fore.YELLOW}ATTACK{Style.RESET_ALL}")

    attack_choice(player_2, player_two_type)
    attack(player_1, weapon_multiplier)

    # Calculate player 1's remaining health points.
    player_one_health = player_one_health - (health * weapon_multiplier)

    print(f"{player_1}: {Fore.GREEN}{player_one_type} has {player_one_health} health points left.{Style.RESET_ALL}")
    print(f"{player_2}: {Fore.YELLOW}took {player_two_turns} turn(s) so far.{Style.RESET_ALL}")
    print("----------------------------------------------")
    print("")

    # Increment player 2 turns count.
    player_two_turns += 1

    # Finish the game if player 1's health falls below 0.
    if player_one_health <= 0:
        print(f"{player_2}: {Fore.GREEN}WINS with {player_two_health} points!!{Style.RESET_ALL} {player_1}: {Fore.RED}LOSES with {player_one_health} points!!{Style.RESET_ALL}")
        exit(0)
