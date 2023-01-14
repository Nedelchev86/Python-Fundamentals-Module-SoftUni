first = input()
second = input()
last_String = first

for i in range(len(first)):
    left_part = second[: i + 1]
    right_part = first[i + 1:]
    current_string = left_part + right_part
    if current_string == last_String:
        continue
    print(current_string)
    last_String = current_string
