"""
name: main.py
author: Uzo Ukekwe
version: python 3.8
purpose: plays a text-based version of mafia with BTS members as users
"""

import random

import gameplay_utilities as gameplay
from art import *

import doctor
import police
import civilian


def print_title():
    """
    Print title art
    """
    bts = text2art("BTS", font='block', chr_ignore=True)
    mafia = text2art("MAFIA", font='block', chr_ignore=True)
    print(gameplay.color1 + bts)
    print(mafia + gameplay.reset)


def login():
    """
    Log in to game and specify town
    :return: username, town
    """
    username = input(gameplay.color2 + "Username:  ")
    while len(username) < 1:
        username = input("Username (must be at least one character):  ")
    input("Password:  ")
    town = input("What will your in-game town be called?:  ")
    while len(town) < 1:
        town = input("What will your in-game town be called? (must be at least one character:  ")

    return username, town


def select_role():
    """
    User is assigned to police officer, doctor, or civilian
    :return: index of role selected
    """
    print(gameplay.reset)             # formatting
    version = input(gameplay.color2 + "Will you \n1) accept a randomized role"
                                      "\n2) choose your role\n")
    versions = ["1", "2"]
    while version not in versions:
        version = input("(You must type 1 or 2.)\n")
    # random role
    if version == "1":
        role = random.randint(0, 2)
    # user picks role
    elif version == "2":
        role = int(input("0) police officer\n1) doctor\n2) civilian\n"))
        roles = [0, 1, 2]
        while role not in roles:
            role = int(input("(You must type 0, 1, or 2.)"))

    return role


def intro(username, town, role_index):
    """
    Set up the user's game
    :param username: name user will see when chatting with players
    :param town: name of the town players will live in
    :param role_index: determines role user will play
    """
    print("Welcome to BTS Mafia! Play at your own risk!\n")
    print("There will be one mafia, one police officer, and one"
          " doctor assigned to this game. Every other player is"
          " a civilian. \nIf you are not the mafia, your job is"
          " to find that player before they find you!\n" + gameplay.reset)

    input(f"Your username is {username}.\nPress enter to continue\n")

    # users enter the game
    players = [username, "namjoon", "seokjin", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    for player in players:
        print(f"{player} has entered {town}.\n")

    roles = ["police officer", "doctor", "civilian"]
    print(f"You are a {roles[role_index]}.")


def main():
    """
    Create gameplay settings and run game
    """
    print_title()
    username, town = login()
    role = select_role()
    intro(username, town, role)

    if role == 0:
        police.play_game(username, town)
    elif role == 1:
        doctor.play_game(username, town)
    elif role == 2:
        civilian.play_game(username, town)


if __name__ == "__main__": 
    main()
