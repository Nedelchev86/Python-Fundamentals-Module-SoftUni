# budget = float(input())
#
# price_for_flour = float(input())
# price_for_eggs = 0.75 * price_for_flour
# price_for_1l_milk = 1.25 * price_for_flour
#
# recepte = price_for_eggs + price_for_flour + (0.25 * price_for_1l_milk)
# colored_egg = 0
# bread_count = 0
#
# while True:
#     budget -= recepte
#     if budget <= 0:
#         budget += recepte
#         break
#     bread_count += 1
#     colored_egg += 3
#     if bread_count % 3 == 0:
#         colored_egg -= (bread_count - 2)
#
# print(F"You made {bread_count} loaves of Easter bread! Now you have {colored_egg} eggs and {budget:.2F}BGN left.")


budget = float(input())

price_for_flour = float(input())
price_for_eggs = 0.75 * price_for_flour
price_for_1l_milk = 1.25 * price_for_flour

recepte = price_for_eggs + price_for_flour + (0.25 * price_for_1l_milk)
colored_egg = 0
bread_count = 0
count = int(budget / recepte)

for i in range(count):
    bread_count += 1
    colored_egg += 3
    if bread_count % 3 == 0:
        colored_egg -= (bread_count - 2)

print(F"You made {count} loaves of Easter bread! Now you have {colored_egg} eggs and {(budget % recepte):.2F}BGN left.")

