divisor = int(input())
boundary = int(input())
max = 0

for i in range(divisor, boundary +1):
    if i % divisor  == 0 and i != 0:
        max = i
print(max)
