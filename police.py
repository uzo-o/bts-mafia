"""
name: police.py
author: Uzo Ukekwe
version: python 3.8
purpose: play the outcome where the user is the police officer
"""

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


    # vote2
    # you are asked to vote to kill someone
    kill2 = input("Who will you vote to kill?\n")

    # while your vote doesn't equal a player you are told to choose someone still in the game
    while kill2 not in live_players:
        if kill2 == username:
            kill2 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill2 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    # if their value = mafia you have a shot of winning and being told they were the mafia
    if role_assignments[kill2] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            new_kill2 = live_players[random.randint(0, 4)]
            while role_assignments[new_kill2] == "mafia":
                new_kill2 = live_players[random.randint(0, 4)]
            print("Your vote was not in the majority. The players have voted to kill "
                  + new_kill2 + ".\n" + new_kill2 + " has exited the game.\n")
            live_players.remove(new_kill2)
        else:
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    # if their value != mafia you are told they were not not the mafia
    elif role_assignments[kill2] != "mafia":
        print("Your vote was in the majority but " + kill2 + " was not the mafia!\n"
              + kill2 + " has exited the game.\n")
        live_players.remove(kill2)

    # night falls
    print("Night has fallen.\n")

    # guess2
    # you are told to guess who the mafia is
    guess2 = input("As the police officer, who do you think is the mafia?\n")
    while guess2 not in live_players:
        if guess2 == username:
            guess2 = input("You cannot guess yourself. Choose again.\n")
        else:
            guess2 = input("You must guess one of the players still in the game. Choose again.\n")

    # you are told if you're right or wrong
    if role_assignments[guess2] == "mafia":
        print(guess2 + " is the mafia!\n")
    elif role_assignments[guess2] != "mafia":
        print(guess2 + " is not the mafia!\n")

    # mafia kills someone who is removed from live_players
    mafia_kill2 = live_players[random.randint(0, (len(live_players) - 1))]
    while role_assignments[mafia_kill2] == "mafia":
        mafia_kill2 = live_players[random.randint(0, 3)]
    # list of ways the player can die
    second_death = [("The mafia microwaved " + mafia_kill2 + " and they have died.\n"),
                    (mafia_kill2 + " was zapped out of existence the mafia.\n"),
                    ("The mafia sat on " + mafia_kill2 + " and they have died.\n"),
                    ("The mafia flooded " + mafia_kill2 + "'s house with tomato juice and they drowned.\n"),
                    (mafia_kill2 + " was embarrassed to death by the mafia in a rap battle.\n")]
    death2 = second_death[random.randint(0, 4)]
    print(death2)
    print(mafia_kill2 + " has exited the game.\n")
    live_players.remove(mafia_kill2)

    # day 3 dialogue (index goes up to 2)
    print("\nDay 3\n(Press enter to advance the chat)\n")
    print("You have one more day to rectify the pivotal situation, police officer.\n"
          "The future of " + town + " is on the line.\nIf the mafia isn't caught, "
                                    "no one will ever return to your Airbnb.")
    input("")

    print(live_players[1] + ":  and then there were 4\n")
    input("")
    print(live_players[0] + ":  we're so close guys\n")
    input("")
    print(username + ":  i think the odds are in our favor\n")
    input("")
    print(live_players[2] + ":  i'm the doctor so don't kill me guys\n")
    input("")
    print(live_players[1] + ":  if you were the doctor why would you tell us\n")
    input("")

    print(live_players[0] + ":  yeah bc now the mafia will kill you so you cant save a civilian\n")
    input("")
    print(live_players[2] + ":  why would i care about that when i can save myself\n")
    input("")
    print(username + ":  points were made\n")
    input("")
    print(live_players[1] + ":  this is such a difficult decision\n")
    input("")
    print(live_players[0] + ":  but you know what would make it easier?\n")
    input("")

    print(live_players[1] + ":  what\n")
    input("")
    print(live_players[0] + ":  voting to kill you\n")
    input("")
    print(live_players[2] + ":  dun dun DUN\n")
    input("")
    print(username + ":  it's not like we have any other leads\n")
    input("")
    print(live_players[1] + ":  i will venmo you guys $4 to not kill me\n")
    input("")

    print(live_players[2] + ":  hmm\n")
    input("")
    print(username + ":  each?\n")
    input("")
    print(live_players[0] + ":  ??? he's a literal stranger think of the big picture\n")
    input("")
    print(live_players[2] + ":  rn im thinking i could get a wendy's 4 for $4 in the next 10 minutes\n")
    input("")
    print(username + ":  wait but is it $4 each? like we don't have to split it?\n")
    input("")

    print(live_players[1] + ":  we can discuss the terms later\n")
    input("")
    print(live_players[2] + ":  sounds good to me let's vote for " + username + "\n")
    input("")
    print(live_players[0] + ":  now there's an idea\n")
    input("")
    print(username + ":  I KNOW Y'ALL LYING \n")
    input("")
    print(live_players[1] + ":  i cant wait to end this game\n")
    input("")

    print(live_players[0] + ":  say no more\n")
    input("")

    # vote3
    # you are asked to vote to kill someone
    kill3 = input("Who will you vote to kill?\n")

    # while your vote doesn't equal a player you are told to choose someone still in the game
    while kill3 not in live_players:
        if kill3 == username:
            kill3 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill3 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    # if their value = mafia you have a shot of winning and being told they were the mafia
    if role_assignments[kill3] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            new_kill3 = live_players[random.randint(0, 2)]
            while role_assignments[new_kill3] == "mafia":
                new_kill3 = live_players[random.randint(0, 2)]
            print("Your vote was not in the majority. The players have voted to kill " + new_kill3 + ".\n"
                  + new_kill3 + " has exited the game.\n")
            live_players.remove(new_kill3)
        else:
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    # if their value != mafia you are told they were not not the mafia
    elif role_assignments[kill3] != "mafia":
        print("Your vote was in the majority but " + kill3 + " was not the mafia!\n"
              + kill3 + " has exited the game.\n")
        live_players.remove(kill3)

    # game over
    mafia_reveal = live_players[random.randint(0, 2)]
    while role_assignments[mafia_reveal] != "mafia":
        mafia_reveal = live_players[random.randint(0, 2)]

    print("The mafia was " + mafia_reveal + "!")
    print("GAME OVER D:  \n")
    time.sleep(10)
