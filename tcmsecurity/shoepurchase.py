#Drew Schmidt 7/15/22
#Python practice from TCM Security's Python for Behginners Course
#final project, shoe budgeting tool

from shoes import Shoes

low = Shoes("And 1s", 30)
medium = Shoes("Air Force 1s", 120)
high = Shoes("Off White", 400)

try:
    shoe_budget = float(input("What is your shoe buget? "))
except ValueError:
    exit("Please enter a number")

for shoes in [high, medium, low]:
    shoes.buy(shoe_budget)


