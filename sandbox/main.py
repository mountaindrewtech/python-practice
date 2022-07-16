savefile = open("savefile.txt")
print(savefile.readlines())
continue_confirmation = input("Do you wish to load this save?: (y/n)")
if continue_confirmation.lower == "y":
    print("Continuing from save!")
elif continue_confirmation.lower == "n":
    print("Returning to menu!")
else:
    print("I didn't quite get that..")