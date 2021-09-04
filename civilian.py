"""
name: civilian.py
author: Uzo Ukekwe
version: python 3.8
purpose: play the outcome where the user is a civilian
"""

import random
import gameplay_utilities as gameplay


def play_game(username, town):
    """
    Play Mafia as a civilian
    :param username: name user sees when chatting with players
    :param town: name of the town players live in
    """
    user_role = "civilian"
    role_assignments = gameplay.assign_roles(user_role)

    # list of people still in game
    live_players = gameplay.player_names
    random.shuffle(live_players)

    # first round
    gameplay.print_morning_intro(1, town, user_role)
    gameplay.run_dialogue(gameplay.get_civilian_dialogue_1(live_players),
                          True, username, live_players)
    gameplay.vote_on_kill(live_players, username, role_assignments)
    gameplay.nighttime(user_role, live_players, username, role_assignments, 1)

    # second round
    gameplay.print_morning_intro(2, town, user_role)
    gameplay.run_dialogue(gameplay.get_civilian_dialogue_2(live_players, username),
                          True, username, live_players)
    gameplay.vote_on_kill(live_players, username, role_assignments)
    victim_2, dummy = gameplay.nighttime(user_role, live_players, username, role_assignments, 2)

    # third round
    gameplay.print_morning_intro(3, town, user_role)
    gameplay.run_dialogue(gameplay.get_civilian_dialogue_3(live_players, username, victim_2),
                          True, username, live_players)
    gameplay.vote_on_kill(live_players, username, role_assignments)

    gameplay.game_over(live_players, role_assignments)