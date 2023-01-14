coffe = 0
while True:
    command = input()
    if command == "END":
        break

    if command == "dog" or command== "cat" or command == "coding" or command == "movie":
        coffe += 1
    elif command == "DOG" or command == "CAT" or command == "CODING" or command == "MOVIE":
        coffe += 2
    else:
        continue
if coffe > 5:
    print("You need extra sleep")
else:
    print((coffe))

