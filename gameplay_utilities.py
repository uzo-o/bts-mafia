"""
name: gameplay_utilities.py
author: Uzo Ukekwe
version: python 3.8
purpose: store functions used among the different modes of mafia
"""

import random
import sys
import time


def assign_roles(user_role):
    """
    Randomly assign a BTS member to a role in the game
    :param user_role: the user's role in the game
    :return: dictionary mapping BTS member to role
    """
    # assign roles to bts members
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian", "police", "mafia", "doctor"]
    roles.remove(user_role)
    role1 = random.choice(roles)
    roles.remove(role1)
    role2 = random.choice(roles)
    roles.remove(role2)
    role3 = random.choice(roles)
    roles.remove(role3)
    role4 = random.choice(roles)
    roles.remove(role4)
    role5 = random.choice(roles)
    roles.remove(role5)
    role6 = random.choice(roles)
    roles.remove(role6)
    role7 = random.choice(roles)
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

    return role_assignments


def print_morning_intro(day, town, user_role):
    """
    Print the text displayed at the beginning of the day
    :param day: current day in town
    :param town: name of town in game
    :param user_role: the user's role in the game
    """
    input(f"\nDay {day}\n(Press enter to advance the chat)")
    if day == 1:
        print(f"The town of {town} used to be considerably safe.\n"
              "The crops grew, the patriarchy was subdued, and "
              "everyone lived in harmony.\nRecently, the killings "
              f"by an alleged mafia have thrown the people of {town} "
              "into a frenzy.\nYou have gathered with some fellow "
              "townspeople to see if you can discover the mafia and "
              "give them a taste of their own medicine.\n")
    elif day == 2:
        if user_role == "police":
            print("Two innocent citizens have died, one at the hands "
                  "of their neighbors and one at the hands of the mafia."
                  "\nTensions have risen and it seems like the conflict "
                  "is getting them nowhere.\nImmediately after the "
                  f"back-to-back funerals, the people of {town} have "
                  "gathered once again to right their wrong.\n")
    elif day == 3:
        if user_role == "police":
            print("You have one more day to rectify the pivotal situation, "
                  f"police officer.\nThe future of {town} is on the line.\n"
                  "If the mafia isn't caught, no one will ever return to "
                  "your Airbnb.\n")


def run_dialogue(dialogue):
    """
    Run through gameplay dialogue
    :param dialogue: lines spoken by players
    """
    for line in dialogue:
        print(line)
        input()


def get_police_dialogue_1(players, username):
    """
    Get a list of dialogue strings for day 1 of police mode
    :param players: list of players still in game
    :param username: name of user playing game
    :return: dialogue strings
    """
    dialogue = [
        f"{players[0]}:  let's kill {players[1]}",
        f"{players[1]}:  we literally just started??",
        f"{players[0]}:  i know but you seem suspicious",
        f"{players[2]}:  we can't just start pointing fingers straight out of the gate",
        f"{username}:  we have to be strategic about this",
        f"{players[2]}:  exactly {username}",
        f"{players[3]}:  then let's pick {players[0]}",
        f"{players[0]}:  THEY NEED PLAYERS LIKE ME THEY NEED PLAYERS LIKE ME"
        f" SO THEY CAN GET ON THEIR KEYBOARDS AND MAKE ME THE BAD GUY CHUN-LI",
        f"{players[4]}:  i say we kill him purely for quoting nicki minaj",
        f"{players[5]}:  good strategy",
        f"{players[6]}:  i don't think we're getting anywhere with this",
        f"{players[2]}:  me neither : (",
        f"{players[1]}:  what do you think {username}?",
        f"{username}:  well i know it's not me",
        f"{players[3]}:  how convincing.",
        f"{players[0]}:  i'm telling you guys the mafia is {players[1]} my hunches are never wrong",
        f"{players[4]}:  well i still think its you boo",
        f"{players[6]}:  maybe it /is/ {username}? they seemed pretty defensive too",
        f"{players[5]}:  all they did was say they weren't the mafia are you dumb",
        f"{username}:  thank you!",
        f"{players[3]}:  we're out of time let's just vote."
    ]

    return dialogue


def get_police_dialogue_2(players, username, victim_1):
    """
    Get a list of dialogue strings for day 2 of police mode
    :param players: list of players still in game
    :param username: name of user playing game
    :param victim_1: player killed on night 1
    :return: dialogue strings
    """
    dialogue = [
        f"{username}:  press f to pay respects for {victim_1}",
        f"{players[3]}:  f",
        f"{players[4]}:  f : <",
        f"{players[2]}:  ok let's focus here",
        f"{players[1]}:  interesting.",
        f"{players[2]}:  what",
        f"{players[1]}:  {players[2]} has no respect for the dead let's kill him",
        f"{players[0]}:  wait tea",
        f"{players[2]}:  ARE YOU PEOPLE SERIOUS",
        f"{players[4]}:  so we're gonna keep picking a scapegoat based off of 0 evidence?",
        f"{username}:  do you want it to be you",
        f"{players[4]}:  on second thought-",
        f"{players[2]}:  OH COME ON",
        f"{players[3]}:  all in favor of killing {players[2]} say aye",
        f"{players[4]}:  that's not even how the voting system works",
        f"{players[0]}:  aye aye captain",
        f"{players[1]}:  does anyone have a better suggestion?",
        f"{username}:  idk but im not really sold on {players[2]}",
        f"{players[0]}:  so let's kill {victim_1}",
        f"{players[3]}:  where were you when {victim_1} died 2 minutes ago",
        f"{players[2]}:  thanks for wasting time again but we need to vote now"
    ]
    
    return dialogue


def get_police_dialogue_3(players, username):
    """
    Get a list of dialogue strings for day 3 of police mode
    :param players: list of players still in game
    :param username: name of user playing game
    :return: dialogue strings
    """
    dialogue = [
        f"{players[1]}:  and then there were 4",
        f"{players[0]}:  we're so close guys",
        f"{username}:  i think the odds are in our favor",
        f"{players[2]}:  i'm the doctor so don't kill me guys",
        f"{players[1]}:  if you were the doctor why would you tell us",
        f"{players[0]}:  yeah bc now the mafia will kill you so you cant save a civilian",
        f"{players[2]}:  why would i care about that when i can save myself",
        f"{username}:  points were made",
        f"{players[1]}:  this is such a difficult decision",
        f"{players[0]}:  but you know what would make it easier?",
        f"{players[1]}:  what",
        f"{players[0]}:  voting to kill you",
        f"{players[2]}:  dun dun DUN",
        f"{username}:  it's not like we have any other leads",
        f"{players[1]}:  i will venmo you guys $4 to not kill me",
        f"{players[2]}:  hmm",
        f"{username}:  each?",
        f"{players[0]}:  ??? he's a literal stranger think of the big picture",
        f"{players[2]}:  rn im thinking i could get a wendy's 4 for $4 in the next 10 minutes",
        f"{username}:  wait but is it $4 each? like we don't have to split it?",
        f"{players[1]}:  we can discuss the terms later",
        f"{players[2]}:  sounds good to me let's vote for {username}",
        f"{players[0]}:  now there's an idea",
        f"{username}:  I KNOW Y'ALL LYING ",
        f"{players[1]}:  i cant wait to end this game",
        f"{players[0]}:  say no more",
    ]

    return dialogue


def get_doctor_dialogue_1(players, username):
    """
    Get a list of dialogue strings for day 1 of doctor mode
    :param players: list of players still in game
    :param username: name of user playing game
    :return: dialogue strings
    """
    dialogue = [
        f"{players[0]}:  how we feeling y'all",
        f"{players[1]}:  people are dying {players[0]}",
        f"{players[0]}:  people that aren't me",
        f"{players[2]}:  yet",
        f"{players[3]}:  just so you guys know i'm the police officer so i better not die",
        f"{username}:  anyone could say that",
        f"{players[4]}:  we need some clues",
        f"{players[5]}:  let me try",
        f"{players[5]}:  do any of you watch friends",
        f"{players[6]}:  you mean the best show in television history?",
        f"{players[5]}:  there's our mafia",
        f"{players[3]}:  yeah we really cant argue with that",
        f"{players[6]}:  OH COME ON ITS A GOOD SHOW",
        f"{players[1]}:  wait i watch full house does that make me a murderer",
        f"{players[2]}:  you're on thin ice",
        f"{username}:  so now we have 2 suspects",
        f"{players[4]}:  thank you for turning yourself in {players[1]}",
        f"{players[1]}:  THAT WASN'T MY INTENTION",
        f"{players[0]}:  so this is going well",
        f"{players[5]}:  we're almost out of time whatever happens doctor pls save me",
        f"{username}:  i hope we're all on the same page here",
    ]

    return dialogue


def vote_on_kill(players, username, role_assignments):
    """
    Everyone votes for their mafia guess
    :param players: players still in game
    :param username: name of user playing game
    :param role_assignments: mapping of BTS player to role
    """
    player_voted = input("Who will you vote to kill?\n")
    while player_voted not in players:
        if player_voted == username:
            player_voted = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            player_voted = input("Your vote must go to killing one of the players still in the game. "
                                 "Choose again.\n")

    # if you guess correctly, your fellow players may or may not agree
    if role_assignments[player_voted] == "mafia":
        if random.randint(0, 1) % 2 == 0:
            # other players vote for a random wrong player
            new_player_voted = random.choice(players)
            while role_assignments[new_player_voted] == "mafia":
                new_player_voted = random.choice(players)
            print(f"Your vote was not in the majority. "
                  f"The players have voted to kill {new_player_voted}.\n"
                  f"{new_player_voted} has exited the game.\n")
            players.remove(new_player_voted)
            input()
        else:
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            sys.exit()
    # you guessed incorrectly
    elif role_assignments[player_voted] != "mafia":
        print(f"Your vote was in the majority but {player_voted} was not the mafia!\n"
              f"{player_voted} has exited the game.\n")
        players.remove(player_voted)


def get_police_kills(victim, night):
    """
    Get a list of mafia killing methods for police gameplay
    :param victim: killed player
    :param night: current night #
    :return: list of kill strings
    """
    first_kills = [
        f"The mafia poisoned {victim}'s almond milk and they have died.\n",
        f"{victim} was ran over multiple times by the mafia.\n",
        f"The mafia danced a two-step on {victim}'s head and they have died.\n",
        f"The mafia emptied {victim}'s fridge except for mustard and they starved to death.\n",
        f"{victim} was seduced off a lethal cliff by the mafia.\n"
    ]
    second_kills = [
        f"The mafia microwaved {victim} and they have died.\n",
        f"{victim} was zapped out of existence the mafia.\n",
        f"The mafia sat on {victim} and they have died.\n",
        f"The mafia flooded {victim}'s house with tomato juice and they drowned.\n",
        f"{victim} was embarrassed to death by the mafia in a rap battle.\n"
    ]

    if night == 1:
        kills = first_kills
    elif night == 2:
        kills = second_kills

    return kills


# FIXME GET DOCTOR KILLS (BOOKMARK)


def mafia_kill(players, role_assignments, user_role, night):
    """
    Mafia kills random player
    :param players: players still in game
    :param role_assignments: mapping of BTS members to roles
    :param user_role: role given to user playing game
    :param night: current night #
    :return: killed player
    """
    killed_player = random.choice(players)
    while role_assignments[killed_player] == "mafia":
        killed_player = random.choice(players)

    if user_role == "police":
        print(random.choice(get_police_kills(killed_player, night)))

    print(f"{killed_player} has exited the game.\n")
    players.remove(killed_player)

    return killed_player


def nighttime(user_role, players, username, role_assignments, night):
    """
    Run through nighttime procedure
    :param user_role: role given to user playing game
    :param players: players still in game
    :param username: name of user playing game
    :param role_assignments: mapping of BTS members to roles
    :param night: current night #
    :return: killed player, saved player
    """
    print("Night has fallen.\n")
    save = ""                   # dummy var when outside doctor mode

    if user_role == "police":
        guess = input("As the police officer, who do you think is the mafia?\n")
        while guess not in players:
            if guess == username:
                guess = input("You cannot guess yourself. Choose again.\n")
            else:
                guess = input("You must guess one of the players still in the game."
                              " Choose again.\n")

        if role_assignments[guess] == "mafia":
            print(f"{guess} is the mafia!\n")
        elif role_assignments[guess] != "mafia":
            print(f"{guess} is not the mafia!\n")

    elif user_role == "doctor":
        save = input("As the doctor, who will you save?\n")
        while save not in players:
            if save == username:
                save = input("Don't be selfish. Choose again.\n")
            else:
                save = input("You must guess one of the players still in the game."
                             " Choose again.\n")

    return mafia_kill(players, role_assignments, user_role, night), save
