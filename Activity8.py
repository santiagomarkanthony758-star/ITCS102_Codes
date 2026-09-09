hobbies = ""  # blank string
18
29*
age = input("What is your age? ")

hb = input("What are your hobbies? ")
hobbies += hb

hb = input("What else? ")
hobbies += ", " + hb

hb = input("Another hobby? ")
hobbies += ", " + hb

print("My age is:", age)
print("My hobbies are:", hobbies)
