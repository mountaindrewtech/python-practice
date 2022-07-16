#Author: Drew Schmidt
#Date: 7/16/22
#Title: Adventure Game
#Description: Python text-based adventure game utilizing everything I've learned so far.

#Imports
import sys
from datetime import datetime
#from playerinfo import Player

#Definitions
def nl():
    print("\n")

#Title Screen
print("-" * 50)
print(" " * 20 + "Adventure Game")
print(" " * 5 + f"Time started: {str(datetime.now())}")
print("-" * 50)

#Start Game
start_game = input("Type \"Play\" to start, \"Continue\" to continue, \"Exit\" to exit: ")

if start_game.lower == "play" or start_game == "p":                                   #should be a for loop until passed into game
    nl()
    Playername = input("Player Name: ")                                               #set to playerinfo class once figured out
elif start_game.lower == "continue" or start_game.lower == "c":
    nl()
    savefile = open("savefile.txt")
    print(savefile.readlines())
    continue_confirmation = input("Do you wish to load this save?: (y/n)")
    if continue_confirmation.lower == "y":
        print("Continuing from save!")
    elif continue_confirmation.lower == "n":
        print("Returning to menu!")
    else:
        print("I didn't quite get that..")
elif start_game.lower == "exit" or start_game == "e" or start_game == "x":
    nl()
    print("Goodbye!")
    sys.exit()
elif start_game.lower == "easter egg":
    nl()
    print("There's no easter eggs in this game.")
else:
    nl()
    print("Type \"Play\" to start, \"Continue\" to continue, \"Exit\" to exit: ")

