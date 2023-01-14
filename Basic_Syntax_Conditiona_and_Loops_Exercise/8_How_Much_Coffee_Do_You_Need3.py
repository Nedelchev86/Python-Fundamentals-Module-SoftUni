coffe = 0
while True:
    command = input()
    if command == "END":
        break

    if command.lower() == "dog" or command.lower() == "cat"\
            or command.lower() == "coding" or command.lower() == "movie":
        if command.islower():
            coffe += 1
        else:
            coffe += 2
if coffe > 5:
    print("You need extra sleep")
else:
    print(coffe)
