
while True:
    command = input()
    if command == "End":
        break
    if command == "SoftUni":
        continue
    new_string = ""
    for i in range(len(command)):
            new_string += (2*command[i])
    print(new_string)

