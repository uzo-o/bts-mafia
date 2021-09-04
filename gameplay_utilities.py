"""
name: gameplay_utilities.py
author: Uzo Ukekwe
version: python 3.8
purpose: store functions used among the different modes of mafia
"""

import random
import sys
import time

# functions are tailored to having 7 other players
player_names = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]


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
        print("Two innocent citizens have died, one at the hands "
              "of their neighbors and one at the hands of the mafia.")
        if user_role == "police":
            print("Tensions have risen and it seems like the conflict "
                  "is getting them nowhere.\nImmediately after the "
                  f"back-to-back funerals, the people of {town} have "
                  "gathered once again to right their wrong.\n")
        elif user_role == "doctor":
            print("The efforts of your work as the doctor will be revealed "
                  "anonymously as the citizens arise this morning.\n"
                  f"The fate of {town} is in your hands.\n")
        elif user_role == "civilian":
            print("You and the other civilians are furious.\n"
                  f"{town} is spiraling into anarchy.\n")
    elif day == 3:
        if user_role == "police":
            print("You have one more day to rectify the pivotal situation, "
                  f"police officer.\nThe future of {town} is on the line.\n"
                  "If the mafia isn't caught, no one will ever return to "
                  "your Airbnb.\n")
        elif user_role == "doctor":
            print("You have one more day to rectify the pivotal situation, "
                  f"doctor.\nThe news of {town} is starting to spread.\n"
                  "By tonight, the town's rating on Niche will be irreparable.\n"
                  "Hopefully you know what you're doing.\n")
        elif user_role == "civilian":
            print("You have one more day to rectify the pivotal situation, "
                  f"civilian.\n{town} is now on Buzzfeed's list of Top 10 "
                  "Uninhabitable Towns.\nBe vigilant and do not take your "
                  "last chance for granted.\n")


def run_dialogue(dialogue, user_is_civilian, username, players):
    """
    Run through gameplay dialogue
    :param dialogue: lines spoken by players
    :param user_is_civilian: true if the user is a civilian, false otherwise
    :param username: name of user playing game
    :param players: players still in game
    """
    for line in dialogue:
        if not user_is_civilian:
            print(line)
            input()
        # civilian gets to enter custom chats & influence player chats
        elif user_is_civilian:
            if line == "user":
                input(f"{username}:  ")
            elif line == "user_effect_1":
                user_said_aye = user_effect_1(username, players)
            elif line == "user_effect_2":
                user_effect_2(username, players, user_said_aye)
            elif line == "user_effect_3":
                user_effect_3(username, players)
            elif line == "user_effect_4":
                user_effect_4(username, players)
            else:
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


def get_doctor_dialogue_2(players, username, save_1):
    """
    Get a list of dialogue strings for day 2 of doctor mode
    :param players: players still in game
    :param username: name of user playing game
    :param save_1: player saved on night 1
    :return: dialogue strings
    """
    dialogue = [
        f"{players[1]}:  unless they saved themselves in which case they deserve to die",
        f"{username}:  guys {save_1} isn't the doctor",
        f"{players[2]}:  how do you know, mafia",
        f"{username}:  ITS NOT ME",
        f"{players[3]}:  let's just have a casual conversation and let the truth come out on its own",
        f"{players[4]}:  so, , , how's the weather for y'all",
        f"{players[0]}:  it's raining where i live",
        f"{players[1]}:  oh yeah i bet its pouring, , , , , , POURING BLOOD, MAFIA",
        f"{username}:  literally what do you be talking about",
        f"{players[2]}:  stay out of this {username} they're on a roll",
        f"{players[3]}:  why can't we ever have a civilized conversation",
        f"{players[1]}:  the way i connected the dots im a mastermind that's all there is to it",
        f"{players[3]}:  never a 'how was your day' or a 'how did you sleep'",
        f"{players[0]}:  do i get a chance to defend myself",
        f"{players[1]}:  no",
        f"{players[2]}:  how many times do we have to teach you this lesson old man",
        f"{username}:  god men really are something",
        f"{players[1]}:  first of all we know second of all we know",
        f"{players[4]}:  i apologize for inciting this violence",
        f"{players[(len(players)) - 1]}:  let's just get this over with"
    ]

    return dialogue


def get_doctor_dialogue_3(players, username, town):
    """
    Get a list of dialogue strings for day 3 of doctor mode
    :param players: players still in game
    :param username: name of user playing game
    :param town: name of town in game
    :return: dialogue strings
    """
    dialogue = [
        f"{players[0]}:  i can't believe we haven't caught the mafia yet",
        f"{players[(len(players)) - 1]}:  let's not waste this day then",
        f"{players[(len(players)) - 2]}:  y'all do realize this is just a game right",
        f"{players[0]}:  shut up didn't you hear that the fate of {town} is in our hands",
        f"{username}:  i am begging y'all to get a hold of yourselves",
        f"{players[2]}:  ok im gonna flip a coin and ill either sacrifice myself or {username}",
        f"{username}:  me???",
        f"{players[1]}:  what does the coin say?",
        f"{players[2]}:  #{username}isoverparty",
        f"{players[0]}:  cancel culture is extremely toxic and i feel"
        " like we as a society have to stop validating this"
        " kind of close-minded behavior",
        f"{username}:  oh ok socrates",
        f"{players[0]}:  : (",
        f"{players[1]}:  whoa this is a bully-free zone {username}",
        f"{players[1]}:  unless of course it's about full house",
        f"{players[2]}:  {username} your tombstone is writing itself",
        f"{username}:  come on guys im like the only one who hasn't tried to deflect by accusing someone else",
        f"{players[0]}:  that's a good point",
        f"{players[0]}:  but you still sound like you would shove me in a locker",
        f"{players[1]}:  that's a you problem {players[0]}",
        f"{players[2]}:  let's all just vote for whoever we want",
        f"{players[(len(players)) - 1]}:  good luck everyone"
    ]

    return dialogue


def user_effect_1(username, players):
    """
    User affects dialogue on day 1 (first time)
    :param username: name of user playing game
    :param players: players still in game
    :return: true if user said aye, false otherwise
    """
    aye = input(f"{username}:  ").strip().lower()
    if aye == "aye":
        print(f"{players[0]}:  ill remember this at the next council meeting {username}")
        user_said_aye = True
    else:
        print(f"{players[0]}:  see {username} has taste")
        user_said_aye = False
    input()

    return user_said_aye


def user_effect_2(username, players, user_said_aye):
    """
    User affects dialogue on day 1 (second time)
    :param username: name of user playing game
    :param players: players still in game
    :param user_said_aye: true if user said aye, false otherwise
    """
    if not user_said_aye:
        print(f"{players[0]}:  at least {username} is on my side. right, {username}?")
        input()
        yes = ["yes", "yeah", "ofc", "of course", "yea", "i am", "ya", "ya i am", "yah",
               "yah i am", "yee", "yee i am", "absolutely", "yes i am", "yeah i am",
               "of course i am", "ofc i am", "yup", "yup i am", "mhm", "sure", "i guess",
               "sure i am", "i guess i am"]
        side = input(f"{username}:  ").strip().lower()
        if side in yes:
            print(f"{players[0]}:  i always liked you kind citizen")
            input()
        else:
            print(f"{players[5]}:  look at the material {players[0]}")
            input()

    else:
        print(f"{players[3]}:  {username} and i are co-founders of the abolish "
              f"{players[0]} movement")
        input()
        print(f"{players[4]}:  wait me too wtf")
        input()
        print(f"{players[5]}:  can we vote out all 3 of you simultaneously")
        input()


def user_effect_3(username, players):
    """
    User affects dialogue on day 2
    :param username: name of user playing game
    :param players: players still in game
    """
    blocklist = ["me", "i do", "i want to", "let's make it", "let's make one",
                 "i want to do it", "can i help?", "let's go", "let's do it",
                 "sure", "i sure do", "i'll help", "let's get it"]
    block = input(f"{username}:  ").strip().lower()
    if block in blocklist:
        print(f"{players[1]}:  justice will be served {username}")
    else:
        print(f"{players[0]}:  {username} would never cosign the obstruction of justice")
    input()


def user_effect_4(username, players):
    """
    User affects dialogue on day 3
    :param username: name of user playing game
    :param players: players still in game
    """
    guess = input(f"{username}:  ")
    if guess == players[0]:
        print(f"{players[0]}:  who would kill this face : <")
    elif guess == players[1]:
        print(f"{players[1]}:  on god??")
    elif guess == players[2]:
        print(f"{players[2]}:  ok mafia")
    else:
        print(f"{players[2]}:  ugh we're out of time")
    

def get_civilian_dialogue_1(players):
    """
    Get a list of dialogue strings for day 1 of civilian mode
    :param players: players still in game
    :return: dialogue strings
    """
    dialogue = [
        f"{players[0]}:  how is everyone doing on this fine morning",
        f"(Don't forget to type your own message when your username comes up!)",
        "user",
        f"{players[1]}:  i'm pretty good irl but we're supposed to be in a town of murderers so",
        f"{players[0]}:  then stay in character killjoy",
        f"{players[2]}:  say aye if you would like to vote for {players[0]} as the town loser",
        "user_effect_1",
        f"{players[3]}:  aye",
        f"{players[4]}:  if i say aye can we please exile him",
        f"{players[5]}:  hey wild idea why don't we exile the mafia first",
        f"{players[6]}:  i'm the police officer and the narrator told me {players[1]} is the mafia",
        f"{players[1]}:  the police officer hasn't even been asked to guess yet\n{players[1]}:  it's day 1 my guy",
        f"{players[6]}:  wait no i've never played this game before don't kill me",
        f"{players[0]}:  the plot thickens as {players[6]} approaches the chopping block. what will become of him?",
        f"{players[2]}:  don't think we forgot you're a lame {players[0]}",
        "user_effect_2",
        f"{players[1]}:  yeah this is kinda wack y'all can put me out of my misery now",
        f"{players[6]}:  don't be a quitter {players[1]} : (",
        f"{players[2]}:  if we're killing people for fun may i make a suggestion",
        f"{players[0]}:  killing people for kicks?? you better have an airtight alibi, buddy",
        f"{players[4]}:  i'm shaking literally who talks like that",
        f"{players[6]}:  he might be a baby boomer let's just respect our elders",
        f"{players[3]}:  ok is everyone ready?",
        "user"
    ]

    return dialogue


def get_civilian_dialogue_2(players, username):
    """
    Get a list of dialogue strings for day 2 of civilian mode
    :param players: players still in game
    :param username: name of user playing game
    :return: dialogue strings
    """
    dialogue = [
        f"{players[1]}:  another one bites the dust",
        f"{players[0]}:  *two",
        f"{players[1]}:  can you block people in this game",
        f"{players[2]}:  right so does anyone have a case for why they're not the mafia",
        "user",
        f"{players[3]}:  [gasp] it's {username}",
        f"{players[4]}:  they do seem pretty defensive nice work {players[3]}",
        f"{players[1]}:  at this point i can't tell if y'all are serious or not",
        f"{players[2]}:  can we hear other people's defenses too??",
        f"{players[3]}:  as you can tell from my lightning speed investigative work i'm the police officer",
        f"{players[4]}:  oh ok that makes sense",
        f"{players[1]}:  does it actually {players[4]}",
        f"{players[4]}:  is {players[1]} conspiring with {username}",
        "user",
        f"{players[4]}:  we didn't ask you",
        f"{players[0]}:  well my defense is that i'm too morally righteous to be a killer",
        f"{players[1]}:  who wants to make a blocklist with me",
        "user_effect_3",
        f"{players[2]}:  anyone ELSE have a viable case to present",
        f"{players[3]}:  wait a second why do you keep asking everyone else to talk",
        f"{players[0]}:  just so you know i never questioned you {players[2]} so please don't strangle me",
        f"{players[2]}:  IM NOT GONNA STRANGLE ANYONE IM NOT THE MAFIA",
        f"{players[1]}:  do you believe him {username}?",
        "user",
        f"{players[1]}:  i'll follow your lead",
    ]
    
    return dialogue


def get_civilian_dialogue_3(players, username, victim_2):
    """
    Get a list of dialogue strings for day 3 of civilian mode
    :param players: players still in game
    :param username: name of user playing game
    :param victim_2: player killed by mafia on night 2
    :return: dialogue strings
    """
    dialogue = [
        f"{players[1]}:  we're officially screwed",
        f"{players[0]}:  c'mon we can still turn this around",
        f"{players[2]}:  {victim_2} was so young, , , he had so much to live for",
        f"{players[1]}:  we don't even know his age",
        f"{players[2]}:  i know i just wanted something to type too",
        "user",
        f"{players[1]}:  let's listen to {username} they haven't said anything dumb so far",
        "user",
        f"{players[0]}:  ty for your input",
        f"{players[2]}:  now let's do the exact opposite of anything {username} says",
        f"{players[1]}:  WHY",
        f"{players[2]}:  idk just to shake things up",
        f"{players[0]}:  some people just want to see the world burn : (",
        f"{players[2]}:  did {players[0]} just confess to arson",
        "user",
        f"{players[1]}:  quick question {players[2]} are you a flat earther",
        f"{players[2]}:  none of us have seen the earth from space anything is possible",
        f"{players[1]}:  this explains a lot",
        f"{players[0]}:  wait i want to hear his argument",
        "user",
        f"{players[1]}:  so this town is doomed",
        f"{players[0]}:  not if we're optimistic!",
        f"{players[1]}:  sorry\n{players[1]}:  this town is doomed!! : D <3",
        f"{players[2]}:  let's cut to the chase who do you all think the mafia is",
        "user_effect_4"
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
    Get a list of mafia killing methods for police mode
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


def get_doctor_kills(victim, night):
    """
    Get a list of mafia killing methods for doctor mode
    :param victim: killed player
    :param night: current night #
    :return: list of kill strings
    """
    first_kills = [
        f"The mafia stole {victim}'s cat and they died of grief.\n",
        f"{victim} was flexed on by the mafia. It was fatal.\n",
        f"The mafia used {victim}'s head as a golf ball and they have died.\n",
        f"The mafia threw {victim} into a volcano.\n",
        f"The mafia practiced the heimlich on {victim}. "
        f"Unfortunately, the maneuver is fatal when performed incorrectly.\n"
    ]
    second_kills = [
        f"The mafia steamrolled {victim} and they have died.\n",
        f"{victim} was trapped in a washing machine by the mafia.\n",
        f"The mafia rerouted {victim}'s GPS and they drove into the Atlantic Ocean.\n",
        f"The mafia teleported {victim} into a black hole.\n",
        f"{victim} was turned into stone after making eye contact with the mafia.\n"
    ]

    if night == 1:
        kills = first_kills
    elif night == 2:
        kills = second_kills

    return kills


def get_civilian_kills(victim, night):
    """
    Get a list of mafia killing methods for civilian mode
    :param victim: killed player
    :param night: current night #
    :return: list of kill strings
    """
    first_kills = [
        f"The mafia forced {victim} to listen to bass boosted country music "
        f"for 10 hours and they passed away.\n",
        f"{victim}'s knee caps were stolen by the mafia. It was fatal.\n",
        f"The mafia summoned a tornado in {victim}'s house.\n",
        f"The mafia threw {victim} under the bus. Not metaphorically. They're dead.\n",
        f"{victim} was pranked by the mafia. This prank went horribly wrong.\n"
    ]
    second_kills = [
        f"The mafia slapped {victim} into next week and they have died.\n",
        f"{victim} was trapped in a lion den by the mafia.\n",
        f"The mafia spilled scalding hot coffee on {victim}'s entire body."
        f" They could not recover.\n",
        f"The mafia told Thanos to snap {victim}'s life away.\n",
        f"{victim} was entranced by the mafia and agreed to stick a fork "
        f"into an electrical socket.\n"
    ]

    if night == 1:
        kills = first_kills
    elif night == 2:
        kills = second_kills

    return kills


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
    elif user_role == "doctor":
        print(random.choice(get_doctor_kills(killed_player, night)))
    elif user_role == "civilian":
        print(random.choice(get_civilian_kills(killed_player, night)))

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
    save = ""  # dummy var when outside doctor mode

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


def doctor_save_outcome(victim, save, players, night):
    """
    Reveal the outcome of the doctor's choice to save a player
    :param victim: the last player killed
    :param save: the player saved by the mafia
    :param players: players still in the game
    :param night: the night the save took place
    """
    if save == victim:
        print(f"The doctor saved {save} and they have been revived.\n"
              f"{save} has entered the game.\n")
        players.append(save)
    else:
        print(f"The doctor protected {save} and they are still in the game.\n")

    if night == 1:
        if save != players[0]:
            print(f"{players[0]}:  so i guess {save} isn't the doctor?\n")
        else:
            print(f"{players[(len(players)) - 1]}:  so i guess {save} isn't the doctor?\n")
        input()


def game_over(players, role_assignments):
    """
    Reveal the mafia and end the game
    :param players: players still in game
    :param role_assignments: mapping of BTS members to roles
    """
    mafia_reveal = random.choice(players)
    while role_assignments[mafia_reveal] != "mafia":
        mafia_reveal = random.choice(players)
    print(f"The mafia was {mafia_reveal}!")
    print("GAME OVER D:\n")
    time.sleep(10)
    sys.exit()
