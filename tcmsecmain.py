#Print String

print("Hello world!")
print('Hello world!')
#Triple quotes prints multiple lines
print("""This string runs
multiple lines""")
#We can also concatonate
print("This string" + " concatonates") 
#New line
print('\n')
print('Test out that new line')

print('\n')
#MATH
print(50 +50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #pemdas
print(50 ** 50) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 /6) #division with remainder
print(50 // 6) #no remainder

print('\n')
#VARIABLES AND METHODS
quote = 'All is fair in love and war.'
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters

name = "Drew" #string
age = 22 #int
gpa = 3.8 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #will it round? NO.

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print(age)

birthday = 1

age += birthday
print(age)

print('\n')
#FUNCTIONS

def who_am_i(): #this is a function without parameters
    name = "Drew" #local variable
    age = 22
    print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)

def add(x,y):
    print(x + y)

add(7,7)

def multiply(x,y):
    return x * y

multiply(7,7)
print(multiply(7,7))

def square_root(x):
    print(x ** .5)

square_root(64)

def nl():
    print('\n')

nl()
#BOOLEAN EXPRESSIONS (TRUE OR FALSE)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()
#RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False

nl()
#CONDITIONAL STATEMENTS - if/else

def drink(money):
    if money >= 2:
        return "You got yourself a drink!"
    else:
        return "No drink for you!"

print(drink(3))
print(drink(1))

nl()

def alcohol(age,money):
    if(age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21 and money < 5):
        return "Come back with more money."
    elif (age < 21) and (money >= 5):
        return "Nice try kid!"
    else:
        return "You're too young and too poor."

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

nl()
#LISTS - Have brackets []
movies = ["When Harry Met Sally", "The Hangover", "The Perks of Being a Wallflower", "The Exorcist"]

print(movies[1]) #returns the second item in the list
print(movies[0]) #returns the first item in the list
print(movies[1:3]) #returns the first index item given right until the last number, but not include the last number; 2 items
print(movies[1:])
print(movies[:1])
print(movies[-1]) #returns last item in list

print(len(movies)) #counts items in list
movies.append("JAWS") #appends to end of list
print(movies)

movies.insert(2, "Hustle")
print(movies)

movies.pop() #removes the last item
print(movies)

movies.pop(0) #removes the first item
print(movies)

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies
print(our_favorite_movies)

grades = [["Bob", 82], ["Alice", 90], ["Jeff", 73]]
bobs_grade = grades[0][1]
print(bobs_grade)

grades[0][1] = 83
print(grades)

nl()
#TUPLES - Like lists, do not change, uses () - inmutable
grades = ("a", "b", "c", "d", "f")

print(grades[1])

nl()
#LOOPING

#For loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
    print(x)

#ip = 1..254
#for x in ip:
#    ping 192.168.1.x

#While loops - execute as long as True
i = 1

while i < 10:
    print(i)
    i += 1

nl()
#ADVANCED STRINGS

my_name = "Drew"
print(my_name[0]) #first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence"
print(sentence[:4])
print(sentence.split()) #delimitter - default is a space

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)

quote = "He said, 'give me all your money'"
print(quote)
quote = "He said, \"give me all your money.\""
print(quote)

too_much_space = "             hello      "
print(too_much_space.strip())

print("A" in "Apple") #True
print("a" in "Apple") #False

letter = "A"
word = "Apple"
print(letter.lower() in word.lower()) #improved

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movi is %s." % movie)
print(f"My favorite movie is {movie}.") #latest method

nl()
#DICTIONARIES - key/value pairs {}

drinks = {"White Russion": 7, "Old Fashioned": 10, "Lemon Drop": 8} #drink is the key value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene", "Louise", "Teddy"], "HR": ["Jimmy Jr.", "Mort"]}
print(employees)
employees["Legal"] = ["My. Frond"] #adds new key:value pair
print(employees)

employees.update({"Sales": ["Andie", "Ollie"]}) #adds new key:value pair as well
print(employees)

drinks["White Russian"] = 8
print(drinks)

print(drinks.get("White Russian"))

nl()