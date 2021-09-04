"""
name: police.py
author: Uzo Ukekwe
version: python 3.8
purpose: play the outcome where the user is the police officer
"""
import sys
import time
import random
import gameplay_utilities as gameplay


def play_game(username, town):
    """
    Play mafia as the police officer
    :param username: name user sees when chatting with players
    :param town: name of the town players live in
    """
    user_role = "police"
    role_assignments = gameplay.assign_roles(user_role)

    # list of people still in game
    live_players = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    random.shuffle(live_players)

    # first round
    gameplay.print_morning_intro(1, town, user_role)
    gameplay.run_dialogue(gameplay.get_police_dialogue_1(live_players, username))
    gameplay.vote_on_kill(live_players, username, role_assignments)
    victim_1 = gameplay.nighttime(user_role, live_players, username, role_assignments, 1)

    # second round
    gameplay.print_morning_intro(2, town, user_role)
    gameplay.run_dialogue(gameplay.get_police_dialogue_2(live_players, username, victim_1))
    gameplay.vote_on_kill(live_players, username, role_assignments)
    gameplay.nighttime(user_role, live_players, username, role_assignments, 2)

    # third round
    gameplay.print_morning_intro(3, town, user_role)
    gameplay.run_dialogue(gameplay.get_police_dialogue_3(live_players, username))
    gameplay.vote_on_kill(live_players, username, role_assignments)

    # game over
    mafia_reveal = random.choice(live_players)
    while role_assignments[mafia_reveal] != "mafia":
        mafia_reveal = random.choice(live_players)
    print(f"The mafia was {mafia_reveal}!")
    print("GAME OVER D:\n")
    time.sleep(10)
    sys.exit()
