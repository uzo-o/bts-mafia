"""
name: police.py
author: Uzo Ukekwe
version: python 3.8
purpose: play the outcome where the user is the police officer
"""

import time
import random
import gameplay_functions as gameplay


def play_game(username, town):
    """
    Play mafia as the police officer
    :param username: name user sees when chatting with players
    :param town: name of the town players live in
    """

    # assign roles to bts members
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian", "mafia", "doctor"]
    role1 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role1)
    role2 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role2)
    role3 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role3)
    role4 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role4)
    role5 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role5)
    role6 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role6)
    role7 = roles[random.randint(0, (len(roles) - 1))]
    roles.remove(role7)

    # dictionary of assigned roles
    role_assignments = {
        'seokjin': role1,
        'namjoon': role2,
        'yoongi': role3,
        'hoseok': role4,
        'jimin': role5,
        'taehyung': role6,
        'jungkook': role7
    }

    # list of people still in game
    live_players = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    random.shuffle(live_players)

    # narrator intro
    print("\nDay 1\n(Press enter to advance the chat)\n")
    print("The town of " + town + " used to be considerably safe.\nThe crops grew, the patriarchy"
                                  " was subdued, and everyone lived in harmony.\nRecently, the killings by an alleged mafia"
                                  " have thrown the people of " + town + " into a frenzy.\nYou have gathered with some fellow"
                                                                         " townspeople to see if you can discover the mafia and give them a taste of their own "
                                                                         "medicine.\n")
    input("")

    # dialogue pt 1
    print(live_players[0] + ":  let's kill " + live_players[1] + "\n")
    input("")
    print(live_players[1] + ":  we literally just started??\n")
    input("")
    print(live_players[0] + ":  i know but you seem suspicious\n")
    input("")
    print(live_players[2] + ":  we can't just start pointing fingers straight out of the gate\n")
    input("")
    print(username + ":  we have to be strategic about this\n")
    input("")

    print(live_players[2] + ":  exactly " + username + "\n")
    input("")
    print(live_players[3] + ":  then let's pick " + live_players[0] + "\n")
    input("")
    print(live_players[0] + ":  THEY NEED PLAYERS LIKE ME THEY NEED PLAYERS LIKE ME"
                            " SO THEY CAN GET ON THEIR KEYBOARDS AND MAKE ME THE BAD"
                            " GUY CHUN-LI\n")
    input("")
    print(live_players[4] + ":  i say we kill him purely for quoting nicki minaj\n")
    input("")
    print(live_players[5] + ":  good strategy\n")
    input("")

    print(live_players[6] + ":  i don't think we're getting anywhere with this\n")
    input("")
    print(live_players[2] + ":  me neither : (\n")
    input("")
    print(live_players[1] + ":  what do you think " + username + "?\n")
    input("")
    print(username + ":  well i know it's not me\n")
    input("")
    print(live_players[3] + ":  how convincing.\n")
    input("")

    print(live_players[0] + ":  i'm telling you guys the mafia is " + live_players[1] + " my hunches are never wrong\n")
    input("")
    print(live_players[4] + ":  well i still think its you boo\n")
    input("")
    print(live_players[6] + ":  maybe it /is/ " + username + "? they seemed pretty defensive too\n")
    input("")
    print(live_players[5] + ":  all they did was say they weren't the mafia are you dumb\n")
    input("")
    print(username + ":  thank you!\n")
    input("")

    print(live_players[3] + ":  we're out of time let's just vote.\n")
    input("")

    # you are asked to vote to kill someone
    kill1 = input("Who will you vote to kill?\n")

    # while your vote doesn't equal a player you are told to choose someone still in the game
    while kill1 not in live_players:
        if kill1 == username:
            kill1 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill1 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    # if their value = mafia you have a shot of winning and being told they were the mafia
    if role_assignments[kill1] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            new_kill1 = live_players[random.randint(0, 6)]
            while role_assignments[new_kill1] == "mafia":
                new_kill1 = live_players[random.randint(0, 6)]
            print("Your vote was not in the majority. The players have voted to kill "
                  + new_kill1 + ".\n" + new_kill1 + " has exited the game.\n")
            live_players.remove(new_kill1)
        else:
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    # if their value != mafia you are told they were not not the mafia
    elif role_assignments[kill1] != "mafia":
        print("Your vote was in the majority but " + kill1 + " was not the mafia!\n"
              + kill1 + " has exited the game.\n")
        live_players.remove(kill1)

    # night falls
    print("Night has fallen.\n")

    # you are told to guess who the mafia is
    guess1 = input("As the police officer, who do you think is the mafia?\n")
    while guess1 not in live_players:
        if guess1 == username:
            guess1 = input("You cannot guess yourself. Choose again.\n")
        else:
            guess1 = input("You must guess one of the players still in the game. Choose again.\n")

    # you are told if you're right or wrong
    if role_assignments[guess1] == "mafia":
        print(guess1 + " is the mafia!\n")
    elif role_assignments[guess1] != "mafia":
        print(guess1 + " is not the mafia!\n")

    # mafia kills someone who is removed from live_players
    mafia_kill1 = live_players[random.randint(0, (len(live_players) - 1))]
    while role_assignments[mafia_kill1] == "mafia":
        mafia_kill1 = live_players[random.randint(0, 5)]
    # list of ways the 1st player can die
    first_death = [("The mafia poisoned " + mafia_kill1 + "'s almond milk and they have died.\n"),
                   (mafia_kill1 + " was ran over multiple times by the mafia.\n"),
                   ("The mafia danced a two-step on " + mafia_kill1 + "'s head and they have died.\n"),
                   ("The mafia emptied " + mafia_kill1 + "'s fridge except for mustard and they starved to death.\n"),
                   (mafia_kill1 + " was seduced off a lethal cliff by the mafia.\n")]
    death1 = first_death[random.randint(0, 4)]
    print(death1)
    print(mafia_kill1 + " has exited the game.\n")
    live_players.remove(mafia_kill1)

    # day 2 dialogue (index goes up to 4 now)
    print("\nDay 2\n(Press enter to advance the chat)\n")
    print("Two innocent citizens have died, one at the hands of their neighbors"
          " and one at the hands of the mafia.\nTensions have risen and it seems"
          " like the conflict is getting them nowhere.\nImmediately after the"
          " back-to-back funerals, the people of " + town + " have gathered once"
                                                            " again to right their wrong.\n")
    input("")

    print(username + ":  press f to pay respects for " + mafia_kill1 + "\n")
    input("")
    print(live_players[3] + ":  f\n")
    input("")
    print(live_players[4] + ":  f : <\n")
    input("")
    print(live_players[2] + ":  ok let's focus here\n")
    input("")
    print(live_players[1] + ":  interesting.\n")
    input("")

    print(live_players[2] + ":  what\n")
    input("")
    print(live_players[1] + ":  " + live_players[2] + " has no respect for the dead let's kill him\n")
    input("")
    print(live_players[0] + ":  wait tea\n")
    input("")
    print(live_players[2] + ":  ARE YOU PEOPLE SERIOUS\n")
    input("")
    print(live_players[4] + ":  so we're gonna keep picking a scapegoat based off of 0 evidence?\n")
    input("")

    print(username + ":  do you want it to be you\n")
    input("")
    print(live_players[4] + ":  on second thought-\n")
    input("")
    print(live_players[2] + ":  OH COME ON\n")
    input("")
    print(live_players[3] + ":  all in favor of killing " + live_players[2] + " say aye\n")
    input("")
    print(live_players[4] + ":  that's not even how the voting system works\n")
    input("")

    print(live_players[0] + ":  aye aye captain\n")
    input("")
    print(live_players[1] + ":  does anyone have a better suggestion?\n")
    input("")
    print(username + ":  idk but im not really sold on " + live_players[2] + "\n")
    input("")
    print(live_players[0] + ":  so let's kill " + mafia_kill1 + "\n")
    input("")
    print(live_players[3] + ":  where were you when " + mafia_kill1 + " died 2 minutes ago\n")
    input("")

    print(live_players[2] + ":  thanks for wasting time again but we need to vote now\n")
    input("")

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
