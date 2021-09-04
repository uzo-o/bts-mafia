"""
name: main.py
author: Uzo Ukekwe
version: python 3.8
purpose: plays a text-based version of mafia with BTS members as users
"""

import random
import time
import police


def intro(username, town, position_index):
    """
    Set up the user's game
    :param username: name user will see when chatting with players
    :param town: name of the town players will live in
    :param position_index: determines position user will play
    """
    # greeting + brief instructions
    print("Welcome to BTS Mafia! Play at your own risk!\n")
    print("There will be one mafia, one police officer, and one"
          " doctor assigned to this game. Every other player is"
          " a civilian. \nIf you are not the mafia, your job is"
          " to find that player before they find you!\n")

    input(f"\nYour username is {username}.\nPress enter to continue\n")

    # users enter the game
    players = [username, "namjoon", "seokjin", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    for player in players:
        print(f"{player} has entered {town}.\n")

    positions = ["police officer", "doctor", "civilian"]
    print(f"You are a {positions[position_index]}.")


def doctor(username, town): 
    # if user is a doctor
    # story but with the option to make a character variable = "saved";
    # the mafia will then make their character variable of choice = "killed"
    # but before this so that the doctor can overwrite their choice

    # list of 7 possible bts roles (5 civilians, 1 mafia, 1 doctor)
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian", "mafia", "doctor"]

    # assign an item to the list to a role variable ex. role 1 and then remove that option from the list
    role1 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role1)
    role2 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role2)
    role3 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role3)
    role4 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role4)
    role5 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role5)
    role6 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role6)
    role7 = roles[random.randint(0, (len(roles)-1))]
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
    print("The town of " + town + " used to be considerably safe.\n"
          "The crops grew, the patriarchy was subdued, and everyone lived in harmony.\n"
          "Recently, the killings by an alleged mafia have thrown the people of " + town +
          " into a frenzy.\nYou have gathered with some fellow townspeople to see if you can"
          " discover the mafia and give them a taste of their own medicine.\n")
    input("")

    # dialogue pt 1
    print(live_players[0] + ":  how we feeling y'all\n")
    input("")
    print(live_players[1] + ":  people are dying " + live_players[0] + "\n")
    input("")
    print(live_players[0] + ":  people that aren't me\n")
    input("")
    print(live_players[2] + ":  yet\n")
    input("")
    print(live_players[3] + ":  just so you guys know i'm the police officer so i better not die\n")
    input("")

    print(username + ":  anyone could say that\n")
    input("")
    print(live_players[4] + ":  we need some clues\n")
    input("")
    print(live_players[5] + ":  let me try\n")
    input("")
    print(live_players[5] + ":  do any of you watch friends\n")
    input("")
    print(live_players[6] + ":  you mean the best show in television history?\n")
    input("")

    print(live_players[5] + ":  there's our mafia\n")
    input("")
    print(live_players[3] + ":  yeah we really cant argue with that\n")
    input("")
    print(live_players[6] + ":  OH COME ON ITS A GOOD SHOW\n")
    input("")
    print(live_players[1] + ":  wait i watch full house does that make me a murderer\n")
    input("")
    print(live_players[2] + ":  you're on thin ice\n")
    input("")

    print(username + ":  so now we have 2 suspects\n")
    input("")
    print(live_players[4] + ":  thank you for turning yourself in " + live_players[1] + "\n")
    input("")
    print(live_players[1] + ":  THAT WASN'T MY INTENTION\n")
    input("")
    print(live_players[0] + ":  so this is going well\n")
    input("")
    print(live_players[5] + ":  we're almost out of time whatever happens doctor pls save me\n")
    input("")

    print(username + ":  i hope we're all on the same page here\n")
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
            print("Your vote was not in the majority. The players have voted to kill " + new_kill1 + ".\n"
                  + new_kill1 + " has exited the game.\n")
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

    # you are told to save someone
    save1 = input("As the doctor, who will you save?\n")
    while save1 not in live_players: 
        if save1 == username: 
            save1 = input("Don't be selfish. Choose again.\n")
        else: 
            save1 = input("You must guess one of the players still in the game. Choose again.\n")

    # mafia kills someone who is removed from live_players
    mafia_kill1 = live_players[random.randint(0, (len(live_players)-1))]
    while role_assignments[mafia_kill1] == "mafia": 
        mafia_kill1 = live_players[random.randint(0, 5)]
    # list of ways the 1st player can die
    first_death = [("The mafia stole " + mafia_kill1 + "'s cat and they died of grief.\n"),
                   (mafia_kill1 + " was flexed on by the mafia. It was fatal.\n"),
                   ("The mafia used " + mafia_kill1 + "'s head as a golf ball and they have died.\n"),
                   ("The mafia threw " + mafia_kill1 + " into a volcano.\n"),
                   (mafia_kill1 + " was consensually choked by the mafia."
                    " Unfortunately, the maneuver is fatal when performed incorrectly.\n")]
    death1 = first_death[random.randint(0, 4)]
    print(death1)
    print(mafia_kill1 + " has exited the game.\n")
    live_players.remove(mafia_kill1)

    # day 2 dialogue
    print("\nDay 2\n(Press enter to advance the chat)\n")
    print("Two innocent citizens have died, one at the hands of their"
          " neighbors and one at the hands of the mafia.\n"
          "The efforts of your work as the doctor will be revealed "
          "anonymously as the citizens arise this morning.\nThe fate of "
          + town + " is in your hands.\n")
    input("")

    # if your save matches the mafia kill they are revived and re-added to the list of
    # live players, otherwise they are simply protected from harm
    if save1 == mafia_kill1: 
        print("The doctor saved " + save1 + " and they have been revived.\n" + save1 + " has entered the game.\n")
        live_players.append(save1)
    else: 
        print("The doctor protected " + save1 + " and they are still in the game.\n")

    if save1 != live_players[0]: 
        print(live_players[0] + ":  so i guess " + save1 + " isn't the doctor?\n")
    else: 
        print(live_players[(len(live_players))-1] + ":  so i guess " + save1 + " isn't the doctor?\n")
    input("")
    print(live_players[1] + ":  unless they saved themselves in which case they deserve to die\n")
    input("")
    print(username + ":  guys " + save1 + " isn't the doctor\n")
    input("")
    print(live_players[2] + ":  how do you know, mafia\n")
    input("")
    print(username + ":  ITS NOT ME\n")
    input("")

    print(live_players[3] + ":  let's just have a casual conversation and let the truth come out on its own\n")
    input("")
    print(live_players[4] + ":  so, , , how's the weather for y'all\n")
    input("")
    print(live_players[0] + ":  it's raining where i live\n")
    input("")
    print(live_players[1] + ":  oh yeah i bet its pouring, , , , , , POURING BLOOD, MAFIA\n")
    input("")
    print(username + ":  literally what do you be talking about\n")
    input("")

    print(live_players[2] + ":  stay out of this " + username + " they're on a roll\n")
    input("")
    print(live_players[3] + ":  why can't we ever have a civilized conversation\n")
    input("")
    print(live_players[1] + ":  the way i connected the dots im a mastermind that's all there is to it\n")
    input("")
    print(live_players[3] + ":  never a 'how was your day' or a 'how did you sleep'\n")
    input("")
    print(live_players[0] + ":  do i get a chance to defend myself\n")
    input("")

    print(live_players[1] + ":  no\n")
    input("")
    print(live_players[2] + ":  how many times do we have to teach you this lesson old man\n")
    input("")
    print(username + ":  god men really are useless\n")
    input("")
    print(live_players[1] + ":  first of all we know second of all we know\n")
    input("")
    print(live_players[4] + ":  i apologize for inciting this violence\n")
    input("")

    print(live_players[(len(live_players))-1] + ":  let's just get this over with\n")
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

    # save2
    # you are told to save someone
    save2 = input("As the doctor, who will you save?\n")
    while save2 not in live_players: 
        if save2 == username: 
            save2 = input("Don't be selfish. Choose again.\n")
        else: 
            save2 = input("You must guess one of the players still in the game. Choose again.\n")

    # mafia kills someone who is removed from live_players
    mafia_kill2 = live_players[random.randint(0, (len(live_players)-1))]
    while role_assignments[mafia_kill2] == "mafia": 
        mafia_kill2 = live_players[random.randint(0, 3)]
    # list of ways the player can die
    second_death = [("The mafia steamrolled " + mafia_kill2 + " and they have died.\n"),
                    (mafia_kill2 + " was trapped in a washing machine by the mafia.\n"),
                    ("The mafia rerouted " + mafia_kill2 + "'s GPS and they drove into the Atlantic Ocean.\n"),
                    ("The mafia teleported " + mafia_kill2 + " into a black hole.\n"),
                    (mafia_kill2 + " was turned into stone after making eye contact with the mafia.\n")]
    death2 = second_death[random.randint(0, 4)]
    print(death2)
    print(mafia_kill2 + " has exited the game.\n")
    live_players.remove(mafia_kill2)

    # day 3 dialogue (index goes up to 2)
    print("\nDay 3\n(Press enter to advance the chat)\n")
    print("You have one more day to rectify the pivotal situation, doctor.\nThe news of " + town +
          " is starting to spread.\nBy tonight, the town's rating on Niche will be irreparable.\n"
          "Hopefully you know what you're doing.\n")
    input("")

    # if your save matches the mafia kill they are revived and re-added to the list of live players,
    # otherwise they are simply protected from harm
    if save2 == mafia_kill2: 
        print("The doctor saved " + save2 + " and they have been revived.\n" + save2 + " has entered the game.\n")
        live_players.append(save2)
    else: 
        print("The doctor protected " + save2 + " and they are still in the game.\n")

    print(live_players[0] + ":  i can't believe we haven't caught the mafia yet\n")
    input("")
    print(live_players[(len(live_players))-1] + ":  let's not waste this day then\n")
    input("")
    print(live_players[(len(live_players))-2] + ":  y'all do realize this is just a game right\n")
    input("")
    print(live_players[0] + ":  shut up didn't you hear that the fate of " + town + " is in our hands\n")
    input("")
    print(username + ":  i am begging y'all to get a hold of yourselves\n")
    input("")

    print(live_players[2] + ":  ok im gonna flip a coin and ill either sacrifice myself or " + username + "\n")
    input("")
    print(username + ":  me???\n")
    input("")
    print(live_players[1] + ":  what does the coin say?\n")
    input("")
    print(live_players[2] + ":  # " + username + "isoverparty\n")
    input("")
    print(live_players[0] + ":  cancel culture is extremely toxic and i feel"
                            " like we as a society have to stop validating this"
                            " kind of close-minded behavior\n")
    input("")

    print(username + ":  oh ok socrates\n")
    input("")
    print(live_players[0] + ":  : (\n")
    input("")
    print(live_players[1] + ":  whoa this is a bully-free zone " + username + "\n")
    input("")
    print(live_players[1] + ":  unless of course it's about full house\n")
    input("")
    print(live_players[2] + ":  " + username + " your tombstone is writing itself\n")
    input("")

    print(username + ":  come on guys im like the only one who hasn't tried to deflect by accusing someone else\n")
    input("")
    print(live_players[0] + ":  that's a good point\n")
    input("")
    print(live_players[0] + ":  but you still sound like you would shove me in a locker\n")
    input("")
    print(live_players[1] + ":  that's a you problem " + live_players[0] + "\n")
    input("")
    print(live_players[2] + ":  let's all just vote for whoever we want\n")
    input("")

    print(live_players[(len(live_players))-1] + ":  good luck everyone\n")
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
            print("Your vote was not in the majority. The players have voted to kill "
                  + new_kill3 + ".\n" + new_kill3 + " has exited the game.\n")
            live_players.remove(new_kill3)
        else:
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    # if their value != mafia you are told they were not not the mafia
    elif role_assignments[kill3] != "mafia": 
        print("Your vote was in the majority but " + kill3 + " was not the mafia!\n" + kill3 +
              " has exited the game.\n")
        live_players.remove(kill3)

    # game over
    mafia_reveal = live_players[random.randint(0, 2)]
    while role_assignments[mafia_reveal] != "mafia": 
        mafia_reveal = live_players[random.randint(0, 2)]

    print("The mafia was " + mafia_reveal + "!")
    print("GAME OVER D:  \n")
    time.sleep(10)


def civilian(username, town): 
    # if user is a civilian
    # story without privileges

    # list of 7 possible bts roles (5 civilians, 1 mafia, 1 doctor)
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian", "mafia", "doctor"]

    # assign an item to the list to a role variable ex. role 1 and then remove that option from the list
    role1 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role1)
    role2 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role2)
    role3 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role3)
    role4 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role4)
    role5 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role5)
    role6 = roles[random.randint(0, (len(roles)-1))]
    roles.remove(role6)
    role7 = roles[random.randint(0, (len(roles)-1))]
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
    print("\nDay 1\n(Press enter to advance the chat)\n(Type your own messages when your username comes up)\n")
    print("The town of " + town + " used to be considerably safe.\n"
          "The crops grew, the patriarchy was subdued, and everyone lived in harmony.\n"
          "Recently, the killings by an alleged mafia have thrown the people of " + town +
          " into a frenzy.\nYou have gathered with some fellow townspeople to see if you can"
          " discover the mafia and give them a taste of their own medicine.\n")
    input("")

    # dialogue pt 1
    print(live_players[0] + ":  how is everyone doing on this fine morning\n")
    input("")
    print("(Don't forget to type your own message when your username comes up!)")
    input(username + ":  ")
    print(live_players[1] + ":  i'm pretty good irl but we're supposed to be in a town of murderers so\n")
    input("")
    print(live_players[0] + ":  then stay in character killjoy\n")
    input("")
    print(live_players[2] + ":  say aye if you would like to vote for " + live_players[0] + " as the town loser\n")
    input("")

    aye = input(username + ":  ")
    if aye == "aye": 
        print(live_players[0] + ":  ill remember this at the next council meeting " + username + "\n")
    else: 
        print(live_players[0] + ":  see " + username + " has taste\n")
    input("")
    print(live_players[3] + ":  aye\n")
    input("")
    print(live_players[4] + ":  if i say aye can we please exile him\n")
    input("")
    print(live_players[5] + ":  hey wild idea why don't we exile the mafia first\n")
    input("")

    print(live_players[6] + ":  i'm the police officer and the narrator told me " + live_players[1] + " is the mafia\n")
    input("")
    print(live_players[1] + ":  the police officer hasn't even been asked to guess yet\n" + live_players[1] +
                            ":  it's day 1 my guy\n")
    input("")
    print(live_players[6] + ":  wait no i've never played this game before don't kill me\n")
    input("")
    print(live_players[0] + ":  the plot thickens as " + live_players[6] +
                            " approaches the chopping block. what will become of him?\n")
    input("")
    print(live_players[2] + ":  don't think we forgot you're a lame " + live_players[0] + "\n")
    input("")

    if aye != "aye": 
        print(live_players[0] + ":  at least " + username + " is on my side. right, " + username + "?\n")
        yes = ["yes", "yeah", "ofc", "of course", "yea", "i am", "ya", "ya i am", "yah", "yah i am", "yee",
               "yee i am", "absolutely", "yes i am", "yeah i am", "of course i am", "ofc i am", "yup",
               "yup i am", "mhm", "sure", "i guess", "sure i am", "i guess i am"]
        side = input(username + ":  ")
        if side in yes: 
            print(live_players[0] + ":  i always liked you kind citizen")
            input("")
        else: 
            print(live_players[5] + ":  look at the material " + live_players[0])
            input("")
    else: 
        print(live_players[3] + ":  " + username + " and i are co-founders of the abolish "
              + live_players[0] + " movement\n")
        input("")
        print(live_players[4] + ":  wait me too wtf\n")
        input("")
        print(live_players[5] + ":  can we vote out all 3 of you simultaneously\n")
        input("")
    print(live_players[1] + ":  yeah this is kinda wack y'all can put me out of my misery now\n")
    input("")
    print(live_players[6] + ":  don't be a quitter " + live_players[1] + " : (\n")
    input("")

    print(live_players[2] + ":  if we're killing people for fun may i make a suggestion\n")
    input("")
    print(live_players[0] + ":  killing people for kicks?? you better have an airtight alibi, buddy\n")
    input("")
    print(live_players[4] + ":  i'm shaking literally who talks like that\n")
    input("")
    print(live_players[6] + ":  he might be a baby boomer let's just respect our elders\n")
    input("")
    print(live_players[3] + ":  ok is everyone ready?\n")
    input("")

    input(username + ":  ")

    # you are asked to vote to kill someone
    kill1 = input("Who will you vote to kill?\n")

    # while your vote doesn't equal a player you are told to choose someone still in the game
    while kill1 not in live_players: 
        if kill1 == username: 
            kill1 = input("You cannot vote to kill yourself. Choose again.\n")
        else: 
            kill1 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    # if their value = mafia you have a  shot of winning and being told they were the mafia
    if role_assignments[kill1] == "mafia": 
        if random.randint(0, 100) % 4 == 0: 
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

    # mafia kills someone who is removed from live_players
    mafia_kill1 = live_players[random.randint(0, (len(live_players)-1))]
    while role_assignments[mafia_kill1] == "mafia": 
        mafia_kill1 = live_players[random.randint(0, 5)]
    # list of ways the 1st player can die
    first_death = [("The mafia forced " + mafia_kill1 +
                    " to listen to bass boosted Lil Tay music for 10 hours and they passed away.\n"),
                   (mafia_kill1 + "'s knee caps were stolen by the mafia. It was fatal.\n"),
                   ("The mafia summoned a tornado in " + mafia_kill1 + "'s house.\n"),
                   ("The mafia threw " + mafia_kill1 + " under the bus. Not metaphorically. They're dead.\n"),
                   (mafia_kill1 + " was pranked by the mafia. This prank went horribly wrong.\n")]
    death1 = first_death[random.randint(0, 4)]
    print(death1)
    print(mafia_kill1 + " has exited the game.\n")
    live_players.remove(mafia_kill1)

    # day 2 dialogue
    print("\nDay 2\n(Press enter to advance the chat)\n")
    print("Two innocent citizens have died, one at the hands of their neighbors and one at the hands of the mafia.\n"
          "You and the other civilians are furious.\n" + town + " is spiraling into anarchy.\n")
    input("")

    print(live_players[1] + ":  another one bites the dust\n")
    input("")
    print(live_players[0] + ":  *two\n")
    input("")
    print(live_players[1] + ":  can you block people in this game\n")
    input("")
    print(live_players[2] + ":  right so does anyone have a case for why they're not the mafia\n")
    input("")
    input(username + ":  ")

    print(live_players[3] + ":  [gasp] it's " + username + "\n")
    input("")
    print(live_players[4] + ":  they do seem pretty defensive nice work " + live_players[3] + "\n")
    input("")
    print(live_players[1] + ":  at this point i can't tell if y'all are serious or not\n")
    input("")
    print(live_players[2] + ":  can we hear other people's defenses too??\n")
    input("")
    print(live_players[3] + ":  as you can tell from my lightning speed investigative work i'm the police officer\n")
    input("")

    print(live_players[4] + ":  oh ok that makes sense\n")
    input("")
    print(live_players[1] + ":  does it actually " + live_players[4] + "\n")
    input("")
    print(live_players[4] + ":  is " + live_players[1] + " conspiring with " + username + "\n")
    input("")
    input(username + ":  ")
    print(live_players[4] + ":  we didn't ask you\n")
    input("")

    print(live_players[0] + ":  well my defense is that i'm too morally righteous to be a killer\n")
    input("")
    print(live_players[1] + ":  who wants to make a blocklist with me\n")
    input("")
    blocklist = ["me", "i do", "i want to", "let's make it", "let's make one", "i want to do it",
                 "can i help?", "let's go", "let's do it", "sure", "i sure do", "i'll help", "let's get it"]
    block = input(username + ":  ")
    if block in blocklist: 
        print(live_players[1] + ":  justice will be served " + username + "\n")
    else: 
        print(live_players[0] + ":  " + username + " would never cosign the obstruction of justice\n")
    input("")
    print(live_players[2] + ":  anyone ELSE have a viable case to present\n")
    input("")

    print(live_players[3] + ":  wait a second why do you keep asking everyone else to talk\n")
    input("")
    print(live_players[0] + ":  just so you know i never questioned you " + live_players[2] +
          " so please don't strangle me\n")
    input("")
    print(live_players[2] + ":  IM NOT GONNA STRANGLE ANYONE IM NOT THE MAFIA\n")
    input("")
    print(live_players[1] + ":  do you believe him " + username + "?\n")
    input("")
    input(username + ":  ")

    print(live_players[1] + ":  i'll follow your lead\n")
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

    # if their value = mafia you have a   shot of winning and being told they were the mafia
    if role_assignments[kill2] == "mafia": 
        if random.randint(0, 100) % 4 == 0: 
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
        print("Your vote was in the majority but " + kill2 + " was not the mafia!\n" + kill2 +
              " has exited the game.\n")
        live_players.remove(kill2)

    # night falls
    print("Night has fallen.\n")

    # mafia kills someone who is removed from live_players
    mafia_kill2 = live_players[random.randint(0, (len(live_players)-1))]
    while role_assignments[mafia_kill2] == "mafia": 
        mafia_kill2 = live_players[random.randint(0, 3)]
    # list of ways the player can die
    second_death = [("The mafia slapped " + mafia_kill2 + " into next week and they have died.\n"),
                    (mafia_kill2 + " was trapped in a lion den by the mafia.\n"),
                    ("The mafia spilled scalding hot coffee on " + mafia_kill2 + "'s entire body."
                                                                                 " They could not recover.\n"),
                    ("The mafia told Thanos to snap " + mafia_kill2 + "'s life away.\n"),
                    (mafia_kill2 + " was entranced by the mafia and agreed to"
                                   " stick a fork into an electrical socket.\n")]
    death2 = second_death[random.randint(0, 4)]
    print(death2)
    print(mafia_kill2 + " has exited the game.\n")
    live_players.remove(mafia_kill2)

    # day 3 dialogue (index goes up to 2)
    print("\nDay 3\n(Press enter to advance the chat)\n")
    print("You have one more day to rectify the pivotal situation, civilian.\n" + town +
          " is now on Buzzfeed's list of Top 10 Uninhabitable Towns.\nBe vigilant and do"
          " not take your last chance for granted.\n")
    input("")

    print(live_players[1] + ":  we're officially screwed\n")
    input("")
    print(live_players[0] + ":  c'mon we can still turn this around\n")
    input("")
    print(live_players[2] + ":  " + mafia_kill2 + " was so young, , , he had so much to live for\n")
    input("")
    print(live_players[1] + ":  we don't even know his age\n")
    input("")
    print(live_players[2] + ":  i know i just wanted something to type too\n")
    input("")

    input(username + ":  ")
    print(live_players[1] + ":  let's listen to " + username + " they haven't said anything dumb so far\n")
    input("")
    input(username + ":  ")
    print(live_players[0] + ":  ty for your input\n")
    input("")
    print(live_players[2] + ":  now let's do the exact opposite of anything " + username + " says\n")
    input("")

    print(live_players[1] + ":  WHY\n")
    input("")
    print(live_players[2] + ":  idk just to shake things up\n")
    input("")
    print(live_players[0] + ":  some people just want to see the world burn : (\n")
    input("")
    print(live_players[2] + ":  did " + live_players[0] + " just confess to arson\n")
    input("")
    input(username + ":  ")

    print(live_players[1] + ":  quick question " + live_players[2] + " are you a flat earther\n")
    input("")
    print(live_players[2] + ":  none of us have seen the earth from space anything is possible\n")
    input("")
    print(live_players[1] + ":  this explains a lot\n")
    input("")
    print(live_players[0] + ":  wait i want to hear his argument\n")
    input("")
    input(username + ":  ")

    print(live_players[1] + ":  so this town is doomed\n")
    input("")
    print(live_players[0] + ":  not if we're optimistic!\n")
    input("")
    print(live_players[1] + ":  sorry\n" + live_players[1] + ":  this town is doomed!! : D <3\n")
    input("")
    print(live_players[2] + ":  let's cut to the chase who do you all think the mafia is\n")
    input("")
    guess = input(username + ":  ")
    if guess == live_players[0]: 
        print(live_players[0] + ":  who would kill this face : <\n")
    elif guess == live_players[1]: 
        print(live_players[1] + ":  on god??\n")
    elif guess == live_players[2]: 
        print(live_players[2] + ":  ok mafia\n")
    else: 
        print(live_players[2] + ":  ugh we're out of time\n")

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
        if random.randint(0, 100) % 4 == 0: 
            new_kill3 = live_players[random.randint(0, 2)]
            while role_assignments[new_kill3] == "mafia": 
                new_kill3 = live_players[random.randint(0, 2)]
            print("Your vote was not in the majority. The players have voted to kill " + new_kill3 +
                  ".\n" + new_kill3 + " has exited the game.\n")
            live_players.remove(new_kill3)
        else:
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    # if their value != mafia you are told they were not not the mafia
    elif role_assignments[kill3] != "mafia": 
        print("Your vote was in the majority but " + kill3 + " was not the mafia!\n" + kill3 +
              " has exited the game.\n")
        live_players.remove(kill3)

    # game over
    mafia_reveal = live_players[random.randint(0, 2)]
    while role_assignments[mafia_reveal] != "mafia": 
        mafia_reveal = live_players[random.randint(0, 2)]

    print("The mafia was " + mafia_reveal + "!")
    print("GAME OVER D:  \n")
    time.sleep(10)


# main program
def main():
    """
    Create gameplay settings and run game
    """
    username = input("Username:  ")
    input("Password:  ")
    town = input("What will your in-game town be called?:  ")

    version = input("Will you \n1) accept a randomized role\n2) choose your role\n")
    versions = ["1", "2"]
    while version not in versions: 
        version = input("(You must type 1 or 2.)\n")
    if version == "1": 
        position = random.randint(0, 2)
    elif version == "2": 
        position = int(input("0) police officer\n1) doctor\n2) civilian\n"))
        positions = [0, 1, 2]
        while position not in positions:
            position = int(input("(You must type 0, 1, or 2.)"))

    intro(username, town, position)

    if position == 0:
        police.play_game(username, town)
    elif position == 1:
        doctor(username, town)
    elif position == 2:
        civilian(username, town)


# setup code running main() function
if __name__ == "__main__": 
    main()
