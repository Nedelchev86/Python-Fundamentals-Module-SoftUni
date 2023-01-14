coffee = 0

while True:
    data = input()
    if data == "END":
        print(coffee)
        break
    if data == "coding" or data == "dog" or data == "cat" or data == "movie":
        coffee += 1
    elif data == "CODING" or data == "DOG" or data == "CAT" or data == "MOVIE":
        coffee += 2
    if coffee > 5:
        print("You need extra sleep")
        break
