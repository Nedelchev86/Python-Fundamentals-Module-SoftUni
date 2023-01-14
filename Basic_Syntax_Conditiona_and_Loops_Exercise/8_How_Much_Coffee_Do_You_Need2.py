coffe = 0
lower = ["dog", "cat", "movie", "coding"]
upper = ["DOG", "CAT", "MOVIE", "CODING"]

while True:
    command = input()
    if command == "END":
        print((coffe))
        break

    if command in lower:
        coffe += 1
    elif command in upper:
        coffe += 2
    else:
        continue
    if coffe > 5:
        print("You need extra sleep")
        break

