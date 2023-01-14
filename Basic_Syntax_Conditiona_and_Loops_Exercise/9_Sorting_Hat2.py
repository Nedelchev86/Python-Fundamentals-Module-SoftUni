

while True:
    name = input()
    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break
    if name == "Voldemort":
        print(F"You must not speak of that name!")
        break
    if len(name) < 5:
        print(F"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(F"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(F"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(F"{name} goes to Hufflepuff.")
