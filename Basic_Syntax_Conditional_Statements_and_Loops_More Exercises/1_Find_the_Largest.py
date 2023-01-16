# user_input = input()
# print("".join(sorted(user_input, reverse=True)))


number = input()
for n in range(9, -1, -1):
    for i in number:
        if int(i) == int(n):
            print(n, end="")



# number = input()
#
# number = input()
# print("".join(sorted((number), reverse=True)))
