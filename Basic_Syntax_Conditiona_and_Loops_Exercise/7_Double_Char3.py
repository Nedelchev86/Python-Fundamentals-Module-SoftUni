doube = ""
while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue
    else:
        for i in text:
            doube += 2*i
        print(doube)


