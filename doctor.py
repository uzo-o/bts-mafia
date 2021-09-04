"""
name: doctor.py
author: Uzo Ukekwe
version: python 3.8
purpose: play the outcome where the user is the doctor
"""

import sys
import time
import random
import gameplay_utilities as gameplay


def play_game(username, town):
    """
    Play mafia as the doctor
    :param username: name user sees when chatting with players
    :param town: name of the town players live in
    """
    user_role = "doctor"
    role_assignments = gameplay.assign_roles(user_role)

    # list of people still in game
    live_players = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    random.shuffle(live_players)

    # first round
    gameplay.print_morning_intro(1, town, user_role)
    gameplay.run_dialogue(gameplay.get_doctor_dialogue_1(live_players, username))
    gameplay.vote_on_kill(live_players, username, role_assignments)

