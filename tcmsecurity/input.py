#Drew Schmidt 7/15/22
#Python practice from TCM Security's Python for Behginners Course

#name = input("Enter your name: ")
#drink = input("What's your favorite drink?: ")
#print(f"Hello {name}! Have a {drink}.")

x = float(input("Give me a number: "))
o = input("Give me an operator: ")
y = float(input("Gimme another number: "))
if o == "+":
    print(x + y)
elif o == "-":
    print(x -y)
elif o == "*":
    print(x * y)
elif o == "/":
    print(x / y)
elif o == "**" or "^":
    print(x ** y)
else:
    print("Unknown operator")