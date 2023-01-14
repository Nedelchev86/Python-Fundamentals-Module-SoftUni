a = int(input())
b = int(input())
max_num = 0

for num in range(a, b+1):
    if num % a == 0:
        max_num = num
print(max_num)
