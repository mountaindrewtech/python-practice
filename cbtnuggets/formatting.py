name = "Ben"
age = 42

print("Hello " + name + ", you are", age, "years old.")

print("Hello %s, you are %s years old." % (name,age) )

print("Hello {}, you are {} years old.".format(name, age) )

print(f"Hello {name}, you are {age + 10} years old!")

message = (
    f"Hello {name}, "
    f"you are {age} years old. "
    f"In ten years you'll be {age+10} years old."
)

print(message)