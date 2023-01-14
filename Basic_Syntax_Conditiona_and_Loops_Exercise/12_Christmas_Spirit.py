quantity = int(input())
days_left = int(input())

ornament_set = 2
tree_skirt = 5
garlant = 3
light = 15

spirit = 0
total = 0
for i in range(1, days_left +1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        total += (ornament_set * quantity)
        spirit += 5
    if i % 3 == 0:
        total += (quantity *(tree_skirt + garlant))
        spirit += 13
    if i % 5 == 0:
        total += (quantity * light)
        spirit += 17
    if i % 3 == 0 and i % 5 == 0:
        spirit += 30
    if i % 10 == 0:
        spirit -= 20
        total += (tree_skirt + garlant + light)
if days_left % 10 == 0:
    spirit -= 30

print(F"Total cost: {total}")
print(F"Total spirit: {spirit}")

