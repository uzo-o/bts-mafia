"""
name: main.py
author: Uzo Ukekwe
version: python 3.8
purpose: plays a text-based version of mafia with BTS members as users
"""

import random

import doctor
import police
import civilian


def intro(username, town, position_index):
    """
    Set up the user's game
    :param username: name user will see when chatting with players
    :param town: name of the town players will live in
    :param position_index: determines position user will play
    """
    print("Welcome to BTS Mafia! Play at your own risk!\n")
    print("There will be one mafia, one police officer, and one"
          " doctor assigned to this game. Every other player is"
          " a civilian. \nIf you are not the mafia, your job is"
          " to find that player before they find you!\n")

    input(f"Your username is {username}.\nPress enter to continue\n")

    # users enter the game
    players = [username, "namjoon", "seokjin", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    for player in players:
        print(f"{player} has entered {town}.\n")

    positions = ["police officer", "doctor", "civilian"]
    print(f"You are a {positions[position_index]}.")


def main():
    """
    Create gameplay settings and run game
    """
    username = input("Username:  ")
    while len(username) < 1:
        username = input("Username (must be at least one character):  ")
    input("Password:  ")
    town = input("What will your in-game town be called?:  ")
    while len(town) < 1:
        town = input("What will your in-game town be called? (must be at least one character:  ")

    version = input("Will you \n1) accept a randomized role\n2) choose your role\n")
    versions = ["1", "2"]
    while version not in versions: 
        version = input("(You must type 1 or 2.)\n")
    # random position
    if version == "1": 
        position = random.randint(0, 2)
    # user picks position
    elif version == "2": 
        position = int(input("0) police officer\n1) doctor\n2) civilian\n"))
        positions = [0, 1, 2]
        while position not in positions:
            position = int(input("(You must type 0, 1, or 2.)"))

    intro(username, town, position)

    if position == 0:
        police.play_game(username, town)
    elif position == 1:
        doctor.play_game(username, town)
    elif position == 2:
        civilian.play_game(username, town)


if __name__ == "__main__": 
    main()
