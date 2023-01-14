orders = int(input())
total = 0

for i in range(orders):
    price_for_capsule = float(input())
    days = int(input())
    needed = int(input())
    if price_for_capsule < 0.01 or price_for_capsule > 100000 or days < 1 or days >31 or needed < 1 or needed > 2000:
        continue
    print(F"The price for the coffee is: ${price_for_capsule * days * needed:.2F}")
    total += price_for_capsule * days * needed
print(F"Total: ${total:.2F}")