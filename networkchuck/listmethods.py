#Drew Schmidt
#Network Chuck Python Course

#Adding stuff to lists

supplies = ["tent", "sleeping bag", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 95.5, 10, False]

#supplies.append("toilet paper")

#supplies.append("bidet")

supplies.insert(-2, "example4")

print("This item was just deleted: " + supplies.pop(0))

print(supplies)