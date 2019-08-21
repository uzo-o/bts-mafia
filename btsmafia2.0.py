import random
import time
import contextlib
with contextlib.redirect_stdout(None):
    import pygame
from art import *

from colorama import init
init()

from colorama import Fore, Back, Style

#exe
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
#exe

#bg music
pygame.mixer.init()
pygame.mixer.music.load(resource_path("fakelove.mp3"))
pygame.mixer.music.play(-1,0.0)

#title
bts = text2art("BTS",font='block',chr_ignore=True)
mafia = text2art("MAFIA",font='block',chr_ignore=True)

print(Fore.BLUE + bts)
print(mafia)
print(Fore.WHITE)


def intro(username, town, positionIndex):
    print(Back.BLUE)
    #welcome message
    print("Welcome to BTS Mafia! Play at your own risk!\n")

    #instructions
    print("There will be one mafia, one police officer, and one doctor assigned to this game. Every other player is a civilian. \nIf you are not the mafia, your job is to find that player before they find you!\n")

    #username confirmation
    confirmUser = input("\nYour username is " + username + ".\nPress enter to continue\n")
    print(Style.RESET_ALL)

    #your username has entered the game
    #followed by a list of bts members who have entered the game
    players = [username, "namjoon","seokjin","yoongi","hoseok","jimin","taehyung","jungkook"]
    p = 0
    while p < len(players):
        print(players[p] + " has entered " + town + ".\n")
        p +=1

    #random police officer, doctor, or civilian designation
    positions = ["police officer", "doctor", "civilian"]
    print("You are a " + positions[positionIndex] + ".")

#add paramaters username & town for all 3 functions
def police(username, town):
    #if user is a police officer
    #story but with the option to verify if a character is the mafia, perhaps by putting all character names in a dictionary as keys and giving them values with random roles

    #list of 7 possible bts roles (5 civilians, 1 mafia, 1 doctor)
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian","mafia", "doctor"]

    #assign an item to the list to a role variable ex. role 1 and then remove that option from the list
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

    #dictionary of assigned roles
    roleAssignments = {
        'seokjin':role1,
        'namjoon':role2,
        'yoongi':role3,
        'hoseok':role4,
        'jimin':role5,
        'taehyung':role6,
        'jungkook':role7
    }

    #list of people still in game
    livePlayers = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    random.shuffle(livePlayers)


    #narrator intro
    print("\nDay 1\n(Press enter to advance the chat)\n")
    print("The town of " + town + " used to be considerably safe.\nThe crops grew, the patriarchy was subdued, and everyone lived in harmony.\nRecently, the killings by an alleged mafia have thrown the people of " + town + " into a frenzy.\nYou have gathered with some fellow townspeople to see if you can discover the mafia and give them a taste of their own medicine.\n")
    input("")

    #dialogue pt 1
    print(livePlayers[0] + ": let's kill " + livePlayers[1] + "\n")
    input("")
    print(livePlayers[1] + ": we literally just started??\n")
    input("")
    print(livePlayers[0] + ": i know but you seem suspicious\n")
    input("")
    print(livePlayers[2] + ": we can't just start pointing fingers straight out of the gate\n")
    input("")
    print(username + ": we have to be strategic about this\n")
    input("")

    print(livePlayers[2] + ": exactly " + username + "\n")
    input("")
    print(livePlayers[3] + ": then let's pick " + livePlayers[0] + "\n")
    input("")
    print(livePlayers[0] + ": THEY NEED PLAYERS LIKE ME THEY NEED PLAYERS LIKE ME SO THEY CAN GET ON THEIR F****** KEYBOARDS AND MAKE ME THE BAD GUY CHUN-LI\n")
    input("")
    print(livePlayers[4] + ": i say we kill him purely for quoting nicki minaj\n")
    input("")
    print(livePlayers[5] + ": good strategy\n")
    input("")

    print(livePlayers[6] + ": i don't think we're getting anywhere with this\n")
    input("")
    print(livePlayers[2] + ": me neither :(\n")
    input("")
    print(livePlayers[1] + ": what do you think " + username + "?\n")
    input("")
    print(username + ": well i know it's not me\n")
    input("")
    print(livePlayers[3] + ": how convincing.\n")
    input("")

    print(livePlayers[0] + ": i'm telling you guys the mafia is " + livePlayers[1] + " my hunches are never wrong\n")
    input("")
    print(livePlayers[4] + ": well i still think its you boo\n")
    input("")
    print(livePlayers[6] + ": maybe it /is/ " + username + "? they seemed pretty defensive too\n")
    input("")
    print(livePlayers[5] + ": all they did was say they weren't the mafia are you dumb\n")
    input("")
    print(username + ": thank you!\n")
    input("")

    print(livePlayers[3] + ": we're out of time let's just vote.\n")
    input("")

    #you are asked to vote to kill someone
    kill1 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill1 not in livePlayers:
        if kill1 == username:
            kill1 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill1 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill1] == "mafia":
        if random.randint(0,100) % 2 == 0:
            newKill1 = livePlayers[random.randint(0,6)]
            while roleAssignments[newKill1] == "mafia":
                newKill1 = livePlayers[random.randint(0,6)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill1 + ".\n" + newKill1 + " has exited the game.\n")
            livePlayers.remove(newKill1)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill1] != "mafia":
        print("Your vote was in the majority but " + kill1 + " was not the mafia!\n" + kill1 + " has exited the game.\n")
        livePlayers.remove(kill1)

    #night falls
    print("Night has fallen.\n")

    #you are told to guess who the mafia is
    guess1 =input("As the police officer, who do you think is the mafia?\n")
    while guess1 not in livePlayers:
        if guess1 == username:
            guess1 = input("You cannot guess yourself. Choose again.\n")
        else:
            guess1 = input("You must guess one of the players still in the game. Choose again.\n")

    #you are told if youre right or wrong
    if roleAssignments[guess1] == "mafia":
        print(guess1 + " is the mafia!\n")
    elif roleAssignments[guess1] != "mafia":
        print(guess1 + " is not the mafia!\n" )

    #mafia kills someone who is removed from livePlayers
    mafiaKill1 = livePlayers[random.randint(0, (len(livePlayers)-1))]
    while roleAssignments[mafiaKill1] == "mafia":
        mafiaKill1 = livePlayers[random.randint(0,5)]
    #list of ways the 1st player can die
    firstDeath = [("The mafia poisoned " + mafiaKill1 + "'s almond milk and they have died.\n"), (mafiaKill1 + " was ran over multiple times by the mafia.\n"), ("The mafia danced a two-step on " + mafiaKill1 + "'s head and they have died.\n"), ("The mafia emptied " + mafiaKill1 + "'s fridge except for mustard and they starved to death.\n"), (mafiaKill1 + " was seduced off a lethal cliff by the mafia.\n")]
    death1 = firstDeath[random.randint(0, 4)]
    print(death1)
    print(mafiaKill1 + " has exited the game.\n")
    livePlayers.remove(mafiaKill1)

    #day 2 dialogue (index goes up to 4 now)
    print("\nDay 2\n(Press enter to advance the chat)\n")
    print("Two innocent citizens have died, one at the hands of their neighbors and one at the hands of the mafia.\nTensions have risen and it seems like the conflict is getting them nowhere.\nImmediately after the back-to-back funerals, the people of " + town + " have gathered once again to right their wrong.\n")
    input("")

    print(username + ": press f to pay respects for " + mafiaKill1 + "\n")
    input("")
    print(livePlayers[3] + ": f\n")
    input("")
    print(livePlayers[4] + ": f :<\n")
    input("")
    print(livePlayers[2] + ": ok let's focus here\n")
    input("")
    print(livePlayers[1] + ": interesting.\n")
    input("")

    print(livePlayers[2] + ": what\n")
    input("")
    print(livePlayers[1] + ": " + livePlayers[2] + " has no respect for the dead let's kill him\n")
    input("")
    print(livePlayers[0] + ": wait tea\n")
    input("")
    print(livePlayers[2] + ": ARE YOU PEOPLE SERIOUS\n")
    input("")
    print(livePlayers[4] + ": so we're gonna keep picking a scapegoat based off of 0 evidence?\n")
    input("")

    print(username + ": do you want it to be you\n")
    input("")
    print(livePlayers[4] + ": on second thought-\n")
    input("")
    print(livePlayers[2] + ": OH COME ON\n")
    input("")
    print(livePlayers[3] + ": all in favor of killing " + livePlayers[2] + " say aye\n")
    input("")
    print(livePlayers[4] + ": that's not even how the voting system works\n")
    input("")

    print(livePlayers[0] + ": aye aye captain\n")
    input("")
    print(livePlayers[1] + ": does anyone have a better suggestion?\n")
    input("")
    print(username + ": idk but im not really sold on " + livePlayers[2] +"\n")
    input("")
    print(livePlayers[0] + ": so let's kill " + mafiaKill1 + "\n")
    input("")
    print(livePlayers[3] + ": where were you when " + mafiaKill1 + " died 2 minutes ago\n")
    input("")

    print(livePlayers[2] + ": thanks for wasting time again but we need to vote now\n")
    input("")

    #vote2
    #you are asked to vote to kill someone
    kill2 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill2 not in livePlayers:
        if kill2 == username:
            kill2 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill2 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill2] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            newKill2 = livePlayers[random.randint(0,4)]
            while roleAssignments[newKill2] == "mafia":
                newKill2 = livePlayers[random.randint(0,4)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill2 + ".\n" + newKill2 + " has exited the game.\n")
            livePlayers.remove(newKill2)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill2] != "mafia":
        print("Your vote was in the majority but " + kill2 + " was not the mafia!\n" + kill2 + " has exited the game.\n")
        livePlayers.remove(kill2)

    #night falls
    print("Night has fallen.\n")

    #guess2
    #you are told to guess who the mafia is
    guess2 =input("As the police officer, who do you think is the mafia?\n")
    while guess2 not in livePlayers:
        if guess2 == username:
            guess2 = input("You cannot guess yourself. Choose again.\n")
        else:
            guess2 = input("You must guess one of the players still in the game. Choose again.\n")

    #you are told if youre right or wrong
    if roleAssignments[guess2] == "mafia":
        print(guess2 + " is the mafia!\n")
    elif roleAssignments[guess2] != "mafia":
        print(guess2 + " is not the mafia!\n" )

    #mafia kills someone who is removed from livePlayers
    mafiaKill2 = livePlayers[random.randint(0, (len(livePlayers)-1))]
    while roleAssignments[mafiaKill2] == "mafia":
        mafiaKill2 = livePlayers[random.randint(0,3)]
    #list of ways the player can die
    secondDeath = [("The mafia microwaved " + mafiaKill2 + " and they have died.\n"), (mafiaKill2 + " was zapped out of existence the mafia.\n"), ("The mafia sat on " + mafiaKill2 + " and they have died.\n"), ("The mafia flooded " + mafiaKill2 + "'s house with tomato juice and they drowned.\n"), (mafiaKill2 + " was embarrassed to death by the mafia in a rap battle.\n")]
    death2 = secondDeath[random.randint(0, 4)]
    print(death2)
    print(mafiaKill2 + " has exited the game.\n")
    livePlayers.remove(mafiaKill2)

    #day 3 diaglogue (index goes up to 2)
    print("\nDay 3\n(Press enter to advance the chat)\n")
    print("You have one more day to rectify the pivotal situation, police officer.\nThe future of " + town + " is on the line.\nIf the mafia isn't caught, no one will ever return to your Airbnb.")
    input("")

    print(livePlayers[1] + ": and then there were 4\n")
    input("")
    print(livePlayers[0] + ": we're so close guys\n")
    input("")
    print(username + ": i think the odds are in our favor\n")
    input("")
    print(livePlayers[2] + ": i'm the doctor so don't kill me guys\n")
    input("")
    print(livePlayers[1] + ": if you were the doctor why would you tell us\n")
    input("")

    print(livePlayers[0] + ": yeah bc now the mafia will kill you so you cant save a civilian\n")
    input("")
    print(livePlayers[2] + ": why would i care about that when i can save myself\n")
    input("")
    print(username + ": points were made\n")
    input("")
    print(livePlayers[1] + ": this is such a difficult decision\n")
    input("")
    print(livePlayers[0] + ": but you know what would make it easier?\n")
    input("")

    print(livePlayers[1] + ": what\n")
    input("")
    print(livePlayers[0] + ": voting to kill you\n")
    input("")
    print(livePlayers[2] + ": dun dun DUN\n")
    input("")
    print(username + ": it's not like we have any other leads\n")
    input("")
    print(livePlayers[1] + ": i will venmo you guys $4 to not kill me\n")
    input("")

    print(livePlayers[2] + ": hmm\n")
    input("")
    print(username + ": each?\n")
    input("")
    print(livePlayers[0] + ": ??? he's a literal stranger think of the big picture\n")
    input("")
    print(livePlayers[2] + ": rn im thinking i could get a wendy's 4 for $4 in the next 10 minutes\n")
    input("")
    print(username + ": wait but is it $4 each? like we don't have to split it?\n")
    input("")

    print(livePlayers[1] + ": we can discuss the terms later\n")
    input("")
    print(livePlayers[2] + ": sounds good to me let's vote for " + username + "\n")
    input("")
    print(livePlayers[0] + ": now there's an idea\n")
    input("")
    print(username + ": I KNOW Y'ALL LYING \n")
    input("")
    print(livePlayers[1] + ": i cant wait to end this game\n")
    input("")

    print(livePlayers[0] + ": say no more\n")
    input("")

    #vote3
    #you are asked to vote to kill someone
    kill3 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill3 not in livePlayers:
        if kill3 == username:
            kill3 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill3 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill3] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            newKill3 = livePlayers[random.randint(0,2)]
            while roleAssignments[newKill3] == "mafia":
                newKill3 = livePlayers[random.randint(0,2)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill3 + ".\n" + newKill3 + " has exited the game.\n")
            livePlayers.remove(newKill3)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill3] != "mafia":
        print("Your vote was in the majority but " + kill3 + " was not the mafia!\n" + kill3 + " has exited the game.\n")
        livePlayers.remove(kill3)

    #game over
    mafiaReveal = livePlayers[random.randint(0,2)]
    while roleAssignments[mafiaReveal] != "mafia":
        mafiaReveal = livePlayers[random.randint(0,2)]

    pygame.mixer.stop()
    pygame.mixer.music.load(resource_path("lose.mp3"))
    pygame.mixer.music.play(1,0.0)
    print("The mafia was " + mafiaReveal + "!")
    print("GAME OVER D: \n")
    time.sleep(10)

def doctor(username, town):
    #if user is a doctor
    #story but with the option to make a character variable = "saved"; the mafia will then make their character variable of choice = "killed" but before this so that the doctor can overwrite their choice

    #list of 7 possible bts roles (5 civilians, 1 mafia, 1 doctor)
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian","mafia", "doctor"]

    #assign an item to the list to a role variable ex. role 1 and then remove that option from the list
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

    #dictionary of assigned roles
    roleAssignments = {
        'seokjin':role1,
        'namjoon':role2,
        'yoongi':role3,
        'hoseok':role4,
        'jimin':role5,
        'taehyung':role6,
        'jungkook':role7
    }

    #list of people still in game
    livePlayers = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    random.shuffle(livePlayers)


    #narrator intro
    print("\nDay 1\n(Press enter to advance the chat)\n")
    print("The town of " + town + " used to be considerably safe.\nThe crops grew, the patriarchy was subdued, and everyone lived in harmony.\nRecently, the killings by an alleged mafia have thrown the people of " + town + " into a frenzy.\nYou have gathered with some fellow townspeople to see if you can discover the mafia and give them a taste of their own medicine.\n")
    input("")

    #dialogue pt 1
    print(livePlayers[0] + ": how we feeling y'all\n")
    input("")
    print(livePlayers[1] + ": people are dying " + livePlayers[0] + "\n")
    input("")
    print(livePlayers[0] + ": people that aren't me\n")
    input("")
    print(livePlayers[2] + ": yet\n")
    input("")
    print(livePlayers[3] + ": just so you guys know i'm the police officer so i better not die\n")
    input("")

    print(username + ": anyone could say that\n")
    input("")
    print(livePlayers[4] + ": we need some clues\n")
    input("")
    print(livePlayers[5] + ": let me try\n")
    input("")
    print(livePlayers[5] + ": do any of you watch friends\n")
    input("")
    print(livePlayers[6] + ": you mean the best show in television history?\n")
    input("")

    print(livePlayers[5] + ": there's our mafia\n")
    input("")
    print(livePlayers[3] + ": yeah we really cant argue with that\n")
    input("")
    print(livePlayers[6] + ": OH COME ON ITS A GOOD SHOW\n")
    input("")
    print(livePlayers[1] + ": wait i watch full house does that make me a murderer\n")
    input("")
    print(livePlayers[2] + ": you're on thin ice\n")
    input("")

    print(username + ": so now we have 2 suspects\n")
    input("")
    print(livePlayers[4] + ": thank you for turning yourself in " + livePlayers[1] + "\n")
    input("")
    print(livePlayers[1] + ": THAT WASN'T MY INTENTION\n")
    input("")
    print(livePlayers[0] + ": so this is going well\n")
    input("")
    print(livePlayers[5] + ": we're almost out of time whatever happens doctor pls save me\n")
    input("")

    print(username + ": i hope we're all on the same page here\n")
    input("")

    #you are asked to vote to kill someone
    kill1 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill1 not in livePlayers:
        if kill1 == username:
            kill1 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill1 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill1] == "mafia":
        if random.randint(0,100) % 2 == 0:
            newKill1 = livePlayers[random.randint(0,6)]
            while roleAssignments[newKill1] == "mafia":
                newKill1 = livePlayers[random.randint(0,6)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill1 + ".\n" + newKill1 + " has exited the game.\n")
            livePlayers.remove(newKill1)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill1] != "mafia":
        print("Your vote was in the majority but " + kill1 + " was not the mafia!\n" + kill1 + " has exited the game.\n")
        livePlayers.remove(kill1)

    #night falls
    print("Night has fallen.\n")

    #you are told to save someone
    save1 = input("As the doctor, who will you save?\n")
    while save1 not in livePlayers:
        if save1 == username:
            save1 = input("Don't be selfish. Choose again.\n")
        else:
            save1 = input("You must guess one of the players still in the game. Choose again.\n")

    #mafia kills someone who is removed from livePlayers
    mafiaKill1 = livePlayers[random.randint(0, (len(livePlayers)-1))]
    while roleAssignments[mafiaKill1] == "mafia":
        mafiaKill1 = livePlayers[random.randint(0,5)]
    #list of ways the 1st player can die
    firstDeath = [("The mafia stole " + mafiaKill1 + "'s cat and they died of grief.\n"), (mafiaKill1 + " was flexed on by the mafia. It was fatal.\n"), ("The mafia used " + mafiaKill1 + "'s head as a golf ball and they have died.\n"), ("The mafia threw " + mafiaKill1 + " into a volcano.\n"), (mafiaKill1 + " was consensually choked by the mafia. Unfortunately, the maneuver is fatal when performed incorrectly.\n")]
    death1 = firstDeath[random.randint(0, 4)]
    print(death1)
    print(mafiaKill1 + " has exited the game.\n")
    livePlayers.remove(mafiaKill1)

    #day 2 dialogue
    print("\nDay 2\n(Press enter to advance the chat)\n")
    print("Two innocent citizens have died, one at the hands of their neighbors and one at the hands of the mafia.\nThe efforts of your work as the doctor will be revealed anonymously as the citizens arise this morning.\nThe fate of " + town + " is in your hands.\n")
    input("")

    #if your save matches the mafia kill they are revived and re-added to the list of live players, otherwise they are simply protected from harm
    if save1 == mafiaKill1:
        print("The doctor saved " + save1 + " and they have been revived.\n" + save1 + " has entered the game.\n")
        livePlayers.append(save1)
    else:
        print("The doctor protected " + save1 + " and they are still in the game.\n" )

    if save1 != livePlayers[0]:
        print(livePlayers[0] + ": so i guess " + save1 + " isn't the doctor?\n")
    else:
        print(livePlayers[(len(livePlayers))-1] + ": so i guess " + save1 + " isn't the doctor?\n")
    input("")
    print(livePlayers[1] + ": unless they saved themselves in which case they deserve to die\n")
    input("")
    print(username + ": guys " + save1 + " isn't the doctor\n")
    input("")
    print(livePlayers[2] + ": how do you know, mafia\n")
    input("")
    print(username + ": ITS NOT ME\n")
    input("")

    print(livePlayers[3] + ": let's just have a casual conversation and let the truth come out on its own\n")
    input("")
    print(livePlayers[4] + ": so,,, how's the weather for y'all\n")
    input("")
    print(livePlayers[0] + ": it's raining where i live\n")
    input("")
    print(livePlayers[1] + ": oh yeah i bet its pouring,,,,,, POURING BLOOD, MAFIA\n")
    input("")
    print(username + ": literally what do you be talking about\n")
    input("")

    print(livePlayers[2] + ": stay out of this " + username + " they're on a roll\n")
    input("")
    print(livePlayers[3] + ": why can't we ever have a civilized conversation\n")
    input("")
    print(livePlayers[1] + ": the way i connected the dots im a mastermind thats all there is to it\n")
    input("")
    print(livePlayers[3] + ": never a 'how was your day' or a 'how did you sleep'\n")
    input("")
    print(livePlayers[0] + ": do i get a chance to defend myself\n")
    input("")

    print(livePlayers[1] + ": no\n")
    input("")
    print(livePlayers[2] + ": how many times do we have to teach you this lesson old man\n")
    input("")
    print(username + ": god men really are useless\n")
    input("")
    print(livePlayers[1] + ": first of all we know second of all we know\n")
    input("")
    print(livePlayers[4] + ": i apologize for inciting this violence\n")
    input("")

    print(livePlayers[(len(livePlayers))-1] + ": let's just get this over with\n")
    input("")

    #vote2
    #you are asked to vote to kill someone
    kill2 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill2 not in livePlayers:
        if kill2 == username:
            kill2 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill2 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill2] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            newKill2 = livePlayers[random.randint(0,4)]
            while roleAssignments[newKill2] == "mafia":
                newKill2 = livePlayers[random.randint(0,4)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill2 + ".\n" + newKill2 + " has exited the game.\n")
            livePlayers.remove(newKill2)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill2] != "mafia":
        print("Your vote was in the majority but " + kill2 + " was not the mafia!\n" + kill2 + " has exited the game.\n")
        livePlayers.remove(kill2)

    #night falls
    print("Night has fallen.\n")

    #save2
    #you are told to save someone
    save2 = input("As the doctor, who will you save?\n")
    while save2 not in livePlayers:
        if save2 == username:
            save2 = input("Don't be selfish. Choose again.\n")
        else:
            save2 = input("You must guess one of the players still in the game. Choose again.\n")

    #mafia kills someone who is removed from livePlayers
    mafiaKill2 = livePlayers[random.randint(0, (len(livePlayers)-1))]
    while roleAssignments[mafiaKill2] == "mafia":
        mafiaKill2 = livePlayers[random.randint(0,3)]
    #list of ways the player can die
    secondDeath = [("The mafia steamrolled " + mafiaKill2 + " and they have died.\n"), (mafiaKill2 + " was trapped in a washing machine by the mafia.\n"), ("The mafia rerouted " + mafiaKill2 + "'s GPS and they drove into the Atlantic Ocean.\n"), ("The mafia teleported " + mafiaKill2 + " into a black hole.\n"), (mafiaKill2 + " was turned into stone after making eye contact with the mafia.\n")]
    death2 = secondDeath[random.randint(0, 4)]
    print(death2)
    print(mafiaKill2 + " has exited the game.\n")
    livePlayers.remove(mafiaKill2)

    #day 3 diaglogue (index goes up to 2)
    print("\nDay 3\n(Press enter to advance the chat)\n")
    print("You have one more day to rectify the pivotal situation, doctor.\nThe news of " + town + " is starting to spread.\nBy tonight, the town's rating on Niche will be irreparable.\nHopefully you know what you're doing.\n")
    input("")

    #if your save matches the mafia kill they are revived and re-added to the list of live players, otherwise they are simply protected from harm
    if save2 == mafiaKill2:
        print("The doctor saved " + save2 + " and they have been revived.\n" + save2 + " has entered the game.\n")
        livePlayers.append(save2)
    else:
        print("The doctor protected " + save2 + " and they are still in the game.\n" )

    print(livePlayers[0] + ": i can't believe we haven't caught the mafia yet\n")
    input("")
    print(livePlayers[(len(livePlayers))-1] + ": let's not waste this day then\n")
    input("")
    print(livePlayers[(len(livePlayers))-2] + ": y'all do realize this is just a game right\n")
    input("")
    print(livePlayers[0] + ": shut up didn't you hear that the fate of " + town + " is in our hands\n")
    input("")
    print(username + ": i am begging y'all to get a hold of yourselves\n")
    input("")

    print(livePlayers[2] + ": ok im gonna flip a coin and ill either sacrifice myself or " + username + "\n")
    input("")
    print(username + ": me???\n")
    input("")
    print(livePlayers[1] + ": what does the coin say?\n")
    input("")
    print(livePlayers[2] + ": #" + username + "isoverparty\n")
    input("")
    print(livePlayers[0] + ": cancel culture is extremely toxic and i feel like we as a society have to stop validating this kind of close-minded behavior\n")
    input("")

    print(username + ": oh ok socrates\n")
    input("")
    print(livePlayers[0] + ": :(\n")
    input("")
    print(livePlayers[1] + ": whoa this is a bully-free zone " + username + "\n")
    input("")
    print(livePlayers[1] + ": unless of course it's about full house\n")
    input("")
    print(livePlayers[2] + ": " + username + " your tombstone is writing itself\n")
    input("")

    print(username + ": come on guys im like the only one who hasn't tried to deflect by accusing someone else\n")
    input("")
    print(livePlayers[0] + ": that's a good point\n")
    input("")
    print(livePlayers[0] + ": but you still sound like you would shove me in a locker\n")
    input("")
    print(livePlayers[1] + ": that's a you problem " + livePlayers[0] + "\n")
    input("")
    print(livePlayers[2] + ": let's all just vote for whoever we want\n")
    input("")

    print(livePlayers[(len(livePlayers))-1] + ": good luck everyone\n")
    input("")

    #vote3
    #you are asked to vote to kill someone
    kill3 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill3 not in livePlayers:
        if kill3 == username:
            kill3 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill3 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill3] == "mafia":
        if random.randint(0, 100) % 2 == 0:
            newKill3 = livePlayers[random.randint(0,2)]
            while roleAssignments[newKill3] == "mafia":
                newKill3 = livePlayers[random.randint(0,2)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill3 + ".\n" + newKill3 + " has exited the game.\n")
            livePlayers.remove(newKill3)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill3] != "mafia":
        print("Your vote was in the majority but " + kill3 + " was not the mafia!\n" + kill3 + " has exited the game.\n")
        livePlayers.remove(kill3)

    #game over
    mafiaReveal = livePlayers[random.randint(0,2)]
    while roleAssignments[mafiaReveal] != "mafia":
        mafiaReveal = livePlayers[random.randint(0,2)]

    pygame.mixer.stop()
    pygame.mixer.music.load(resource_path("lose.mp3"))
    pygame.mixer.music.play(1,0.0)
    print("The mafia was " + mafiaReveal + "!")
    print("GAME OVER D: \n")
    time.sleep(10)



def civilian(username, town):
    #if user is a civilian
    #story without privileges

    #list of 7 possible bts roles (5 civilians, 1 mafia, 1 doctor)
    roles = ["civilian", "civilian", "civilian", "civilian", "civilian","mafia", "doctor"]

    #assign an item to the list to a role variable ex. role 1 and then remove that option from the list
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

    #dictionary of assigned roles
    roleAssignments = {
        'seokjin':role1,
        'namjoon':role2,
        'yoongi':role3,
        'hoseok':role4,
        'jimin':role5,
        'taehyung':role6,
        'jungkook':role7
    }

    #list of people still in game
    livePlayers = ["seokjin", "namjoon", "yoongi", "hoseok", "jimin", "taehyung", "jungkook"]
    random.shuffle(livePlayers)


    #narrator intro
    print("\nDay 1\n(Press enter to advance the chat)\n(Type your own messages when your username comes up)\n")
    print("The town of " + town + " used to be considerably safe.\nThe crops grew, the patriarchy was subdued, and everyone lived in harmony.\nRecently, the killings by an alleged mafia have thrown the people of " + town + " into a frenzy.\nYou have gathered with some fellow townspeople to see if you can discover the mafia and give them a taste of their own medicine.\n")
    input("")

    #dialogue pt 1
    print(livePlayers[0] + ": how is everyone doing on this fine morning\n")
    input("")
    print("(Don't forget to type your own message when your username comes up!)")
    input(username +": ")
    print(livePlayers[1] + ": i'm pretty good irl but we're supposed to be in a town of murderers so\n")
    input("")
    print(livePlayers[0] + ": then stay in character killjoy\n")
    input("")
    print(livePlayers[2] + ": say aye if you would like to vote for " + livePlayers[0] + " as the town loser\n")
    input("")

    aye = input(username + ": ")
    if aye == "aye":
        print(livePlayers[0] + ": ill remember this at the next council meeting " + username + "\n")
    else:
        print(livePlayers[0] + ": see " + username + " has taste\n")
    input("")
    print(livePlayers[3] + ": aye\n")
    input("")
    print(livePlayers[4] + ": if i say aye can we please exile him\n")
    input("")
    print(livePlayers[5] + ": hey wild idea why don't we exile the mafia first\n")
    input("")

    print(livePlayers[6] + ": i'm the police officer and the narrator told me " + livePlayers[1] + " is the mafia\n")
    input("")
    print(livePlayers[1] + ": the police officer hasn't even been asked to guess yet\n" + livePlayers[1] + ": it's day 1 my guy\n")
    input("")
    print(livePlayers[6] + ": wait no i've never played this game before don't kill me\n")
    input("")
    print(livePlayers[0] + ": the plot thickens as " + livePlayers[6] + " approaches the chopping block. what will become of him?\n")
    input("")
    print(livePlayers[2] + ": don't think we forgot you're a lame " + livePlayers[0] + "\n")
    input("")

    if aye != "aye":
        print(livePlayers[0] + ": at least " + username + " is on my side. right, " + username + "?\n")
        yes = ["yes", "yeah", "ofc", "of course", "yea", "i am", "ya", "ya i am", "yah", "yah i am", "yee", "yee i am", "absolutely", "yes i am", "yeah i am", "of course i am", "ofc i am", "yup", "yup i am", "mhm", "sure", "i guess", "sure i am", "i guess i am"]
        side = input(username + ": ")
        if side in yes:
            print(livePlayers[0] + ": i always liked you kind citizen")
            input("")
        else:
            print(livePlayers[5] + ": look at the material " + livePlayers[0])
            input("")
    else:
        print(livePlayers[3] + ": " + username + " and i are co-founders of the abolish " + livePlayers[0] + " movement\n")
        input("")
        print(livePlayers[4] + ": wait me too wtf\n")
        input("")
        print(livePlayers[5] + ": can we vote out all 3 of you simultaneously\n")
        input("")
    print(livePlayers[1] + ": yeah this is kinda wack y'all can put me out of my misery now\n")
    input("")
    print(livePlayers[6] + ": don't be a quitter " + livePlayers[1] + " :(\n")
    input("")

    print(livePlayers[2] + ": if we're killing people for fun may i make a suggestion\n")
    input("")
    print(livePlayers[0] + ": killing people for kicks?? you better have an airtight alibi, buddy\n")
    input("")
    print(livePlayers[4] + ": i'm shaking literally who talks like that\n")
    input("")
    print(livePlayers[6] + ": he might be a baby boomer let's just respect our elders\n")
    input("")
    print(livePlayers[3] + ": ok is everyone ready?\n")
    input("")

    input(username + ": ")

    #you are asked to vote to kill someone
    kill1 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill1 not in livePlayers:
        if kill1 == username:
            kill1 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill1 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a  shot of winning and being told they were the mafia
    if roleAssignments[kill1] == "mafia":
        if random.randint(0,100) % 4 == 0:
            newKill1 = livePlayers[random.randint(0,6)]
            while roleAssignments[newKill1] == "mafia":
                newKill1 = livePlayers[random.randint(0,6)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill1 + ".\n" + newKill1 + " has exited the game.\n")
            livePlayers.remove(newKill1)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill1] != "mafia":
        print("Your vote was in the majority but " + kill1 + " was not the mafia!\n" + kill1 + " has exited the game.\n")
        livePlayers.remove(kill1)

    #night falls
    print("Night has fallen.\n")

    #mafia kills someone who is removed from livePlayers
    mafiaKill1 = livePlayers[random.randint(0, (len(livePlayers)-1))]
    while roleAssignments[mafiaKill1] == "mafia":
        mafiaKill1 = livePlayers[random.randint(0,5)]
    #list of ways the 1st player can die
    firstDeath = [("The mafia forced " + mafiaKill1 + " to listen to bass boosted Lil Tay music for 10 hours and they passed away.\n"), (mafiaKill1 + "'s knee caps were stolen by the mafia. It was fatal.\n"), ("The mafia summoned a tornado in " + mafiaKill1 + "'s house.\n"), ("The mafia threw " + mafiaKill1 + " under the bus. Not metaphorically. They're dead.\n"), (mafiaKill1 + " was pranked by the mafia. This prank went horribly wrong.\n")]
    death1 = firstDeath[random.randint(0, 4)]
    print(death1)
    print(mafiaKill1 + " has exited the game.\n")
    livePlayers.remove(mafiaKill1)

    #day 2 dialogue
    print("\nDay 2\n(Press enter to advance the chat)\n")
    print("Two innocent citizens have died, one at the hands of their neighbors and one at the hands of the mafia.\nYou and the other civilians are furious.\n" + town + " is spiraling into anarchy.\n")
    input("")

    print(livePlayers[1] + ": another one bites the dust\n")
    input("")
    print(livePlayers[0] + ": *two\n")
    input("")
    print(livePlayers[1] + ": can you block people in this game\n")
    input("")
    print(livePlayers[2] + ": right so does anyone have a case for why they're not the mafia\n")
    input("")
    input(username + ": ")

    print(livePlayers[3] + ": [gasp] it's " + username + "\n")
    input("")
    print(livePlayers[4] + ": they do seem pretty defensive nice work " + livePlayers[3] + "\n")
    input("")
    print(livePlayers[1] + ": at this point i can't tell if y'all are serious or not\n")
    input("")
    print(livePlayers[2] + ": can we hear other people's defenses too??\n")
    input("")
    print(livePlayers[3] + ": as you can tell from my lightning speed investigative work i'm the police officer\n")
    input("")

    print(livePlayers[4] + ": oh ok that makes sense\n")
    input("")
    print(livePlayers[1] + ": does it actually " + livePlayers[4] + "\n")
    input("")
    print(livePlayers[4] + ": is " + livePlayers[1] + " conspiring with " + username + "\n")
    input("")
    input(username + ": ")
    print(livePlayers[4] + ": we didn't ask you\n")
    input("")

    print(livePlayers[0] + ": well my defense is that i'm too morally righteous to be a killer\n")
    input("")
    print(livePlayers[1] + ": who wants to make a blocklist with me\n")
    input("")
    blocklist = ["me", "i do", "i want to", "let's make it", "let's make one", "i want to do it", "can i help?", "let's go", "let's do it", "sure", "i sure do", "i'll help", "let's get it"]
    block = input(username + ": ")
    if block in blocklist:
        print(livePlayers[1] + ": justice will be served " + username + "\n")
    else:
        print(livePlayers[0] + ": " + username + " would never cosign the obstruction of justice\n")
    input("")
    print(livePlayers[2] + ": anyone ELSE have a viable case to present\n")
    input("")

    print(livePlayers[3] + ": wait a second why do you keep asking everyone else to talk\n")
    input("")
    print(livePlayers[0] + ": just so you know i never questioned you " + livePlayers[2] + " so please don't strangle me\n")
    input("")
    print(livePlayers[2] + ": IM NOT GONNA STRANGLE ANYONE IM NOT THE MAFIA\n")
    input("")
    print(livePlayers[1] + ": do you believe him " + username + "?\n")
    input("")
    input(username + ": ")

    print(livePlayers[1] + ": i'll follow your lead\n")
    input("")

    #vote2
    #you are asked to vote to kill someone
    kill2 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill2 not in livePlayers:
        if kill2 == username:
            kill2 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill2 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a   shot of winning and being told they were the mafia
    if roleAssignments[kill2] == "mafia":
        if random.randint(0, 100) % 4 == 0:
            newKill2 = livePlayers[random.randint(0,4)]
            while roleAssignments[newKill2] == "mafia":
                newKill2 = livePlayers[random.randint(0,4)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill2 + ".\n" + newKill2 + " has exited the game.\n")
            livePlayers.remove(newKill2)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill2] != "mafia":
        print("Your vote was in the majority but " + kill2 + " was not the mafia!\n" + kill2 + " has exited the game.\n")
        livePlayers.remove(kill2)

    #night falls
    print("Night has fallen.\n")

    #mafia kills someone who is removed from livePlayers
    mafiaKill2 = livePlayers[random.randint(0, (len(livePlayers)-1))]
    while roleAssignments[mafiaKill2] == "mafia":
        mafiaKill2 = livePlayers[random.randint(0,3)]
    #list of ways the player can die
    secondDeath = [("The mafia slapped " + mafiaKill2 + " into next week and they have died.\n"), (mafiaKill2 + " was trapped in a lion den by the mafia.\n"), ("The mafia spilled scalding hot coffee on " + mafiaKill2 + "'s entire body. They could not recover.\n"), ("The mafia told Thanos to snap " + mafiaKill2 + "'s life away.\n"), (mafiaKill2 + " was entranced by the mafia and agreed to stick a fork into an electrical socket.\n")]
    death2 = secondDeath[random.randint(0, 4)]
    print(death2)
    print(mafiaKill2 + " has exited the game.\n")
    livePlayers.remove(mafiaKill2)

    #day 3 diaglogue (index goes up to 2)
    print("\nDay 3\n(Press enter to advance the chat)\n")
    print("You have one more day to rectify the pivotal situation, civilian.\n" + town + " is now on Buzzfeed's list of Top 10 Uninhabitable Towns.\nBe vigilant and do not take your last chance for granted.\n")
    input("")

    print(livePlayers[1] + ": we're officially screwed\n")
    input("")
    print(livePlayers[0] + ": c'mon we can still turn this around\n")
    input("")
    print(livePlayers[2] + ": " + mafiaKill2 + " was so young,,, he had so much to live for\n")
    input("")
    print(livePlayers[1] + ": we don't even know his age\n")
    input("")
    print(livePlayers[2] + ": i know i just wanted something to type too\n")
    input("")

    input(username + ": ")
    print(livePlayers[1] + ": let's listen to " + username + " they haven't said anything dumb so far\n")
    input("")
    input(username + ": ")
    print(livePlayers[0] + ": ty for your input\n")
    input("")
    print(livePlayers[2] + ": now let's do the exact opposite of anything " + username + " says\n")
    input("")

    print(livePlayers[1] + ": WHY\n")
    input("")
    print(livePlayers[2] + ": idk just to shake things up\n")
    input("")
    print(livePlayers[0] + ": some people just want to see the world burn :(\n")
    input("")
    print(livePlayers[2] + ": did " + livePlayers[0] + " just confess to arson\n")
    input("")
    input(username + ": ")

    print(livePlayers[1] + ": quick question " + livePlayers[2] + " are you a flat earther\n")
    input("")
    print(livePlayers[2] + ": none of us have seen the earth from space anything is possible\n")
    input("")
    print(livePlayers[1] + ": this explains a lot\n")
    input("")
    print(livePlayers[0] + ": wait i want to hear his argument\n")
    input("")
    input(username + ": ")

    print(livePlayers[1] + ": so this town is doomed\n")
    input("")
    print(livePlayers[0] + ": not if we're optimistic!\n")
    input("")
    print(livePlayers[1] + ": sorry\n" + livePlayers[1] + ": this town is doomed!! :D <3\n")
    input("")
    print(livePlayers[2] + ": let's cut to the chase who do you all think the mafia is\n")
    input("")
    guess = input(username + ": ")
    if guess == livePlayers[0]:
        print(livePlayers[0] + ": who would kill this face :<\n")
    elif guess == livePlayers[1]:
        print(livePlayers[1] + ": on god??\n")
    elif guess == livePlayers[2]:
        print(livePlayers[2] + ": ok mafia\n")
    else:
        print(livePlayers[2] + ": ugh we're out of time\n")

    input("")

    #vote3
    #you are asked to vote to kill someone
    kill3 = input("Who will you vote to kill?\n")

    #while your vote doesn't equal a player you are told to choose someone still in the game
    while kill3 not in livePlayers:
        if kill3 == username:
            kill3 = input("You cannot vote to kill yourself. Choose again.\n")
        else:
            kill3 = input("Your vote must go to killing one of the players still in the game. Choose again.\n")

    #if their value = mafia you have a shot of winning and being told they were the mafia
    if roleAssignments[kill3] == "mafia":
        if random.randint(0, 100) % 4 == 0:
            newKill3 = livePlayers[random.randint(0,2)]
            while roleAssignments[newKill3] == "mafia":
                newKill3 = livePlayers[random.randint(0,2)]
            print("Your vote was not in the majority. The players have voted to kill " + newKill3 + ".\n" + newKill3 + " has exited the game.\n")
            livePlayers.remove(newKill3)
        else:
            pygame.mixer.stop()
            pygame.mixer.music.load(resource_path("win.mp3"))
            pygame.mixer.music.play(1,0.0)
            print("You won! The mafia has been caught!\n")
            time.sleep(10)
            exit()
    #if their value != mafia you are told they were not not the mafia
    elif roleAssignments[kill3] != "mafia":
        print("Your vote was in the majority but " + kill3 + " was not the mafia!\n" + kill3 + " has exited the game.\n")
        livePlayers.remove(kill3)

    #game over
    mafiaReveal = livePlayers[random.randint(0,2)]
    while roleAssignments[mafiaReveal] != "mafia":
        mafiaReveal = livePlayers[random.randint(0,2)]

    pygame.mixer.stop()
    pygame.mixer.music.load(resource_path("lose.mp3"))
    pygame.mixer.music.play(1,0.0)
    print("The mafia was " + mafiaReveal + "!")
    print("GAME OVER D: \n")
    time.sleep(10)


#main program
def main():
    you = input("Username: ")
    hasNoEffect = input("Password: ")
    location = input("What will your in-game town be called?: ")
    version = input("Will you \n1) accept a randomized role\n2) choose your role\n")
    versions = ["1","2"]
    while version not in versions:
        version = input("(You must type 1 or 2.)\n")
    if version == "1":
        gameMode = random.randint(0, 2)
    elif version == "2":
        gameMode = int(input("0) police officer\n1) doctor\n2) civilian\n"))
        gameModes = [0, 1, 2]
        while gameMode not in gameModes:
            gameMode = int(input("(You must type 0, 1, or 2.)"))
    intro(you, location, gameMode)
    if gameMode == 0:
        police(you, location)
    elif gameMode == 1:
        doctor(you, location)
    elif gameMode == 2:
        civilian(you, location)

#setup code running main() function
if __name__ == "__main__":
  main()
