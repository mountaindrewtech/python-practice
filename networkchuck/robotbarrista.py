#Drew Schmidt
#Network Chuck Python Course

#Let's start a coffee shop together!! We're going to build a coffee shop using some new Python programming concepts!!

#Let's build robot Barista!!

print("Hello, welcome")

name = input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
  evil_status = input("Are you evil?\n")
  if evil_status == "Yes" and 4 > int(input("How many good deeds have you done today?\n")):
  
    print("You're not welcome here Evil " + name + "!! Get out!!")
    exit()
  else:
    print("Oh, so you're one of those good " + name + "'s. Come on in!!")
else:
  print("Hello " + name + ", thank you so much for coming in today\n\n\n")

menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"

order = input("Here's the menu " + name +", what would you like? We curently have these picks to choose from.\n" + menu + "\n")

add = 0

if order == "Frappuccino":
  price = 13
elif order == "Black Coffee":
  price = 3
elif order == "Espresso":
  price = 5
elif order == "Cappuccino":
  price = 10
elif order == "Latte":
  price = 9
  whip = input("Would you like whipped cream with that?\n")
  if whip == "Yes":
    add = 2
  else:
    add = 0
else:
  print("Sorry, we don't have that here.")
  price = 0

quantity = input("No problem " + name + ", how many " + order + "'s would you like?\n")

total =  price * int(quantity) + add

print(total)
print("Okay " + name + ", your total is $" + str(total) + "!\n" + "Your " + quantity +" " + order + "'s will be right up!")