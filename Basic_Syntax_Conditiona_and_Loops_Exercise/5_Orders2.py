number_of_orders = int(input())
total_for_order = 0
total = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100000 or days < 1 or days > 31 or needed_per_day < 1 or needed_per_day > 2000:
        continue
    total_for_order = price_per_capsule * days * needed_per_day
    print(F"The price for the coffee is: ${total_for_order:.2F}")
    total += total_for_order
print(F"Total: ${total:.2F}")