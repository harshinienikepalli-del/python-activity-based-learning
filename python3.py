budget = int(input("Enter your budget: "))
n = int(input("Enter number of products: "))

prices = []
quantity = []
total = 0

for i in range(n):
    p = int(input("Enter product price: "))
    q = int(input("Enter quantity: "))

    prices.append(p)
    quantity.append(q)

    total += p * q

print("Total bill:", total)

if total >= 1000:
    total = total * 90 / 100
    print("After 10% discount:", total)

while total > budget:
    for i in range(n - 1, -1, -1):
        if total <= budget:
            break

        if quantity[i] > 0:
            quantity[i] -= 1
            print("Reduced one item from product", i + 1)

            total = 0
            for j in range(n):
                total += prices[j] * quantity[j]

            if total >= 1000:
                total = total * 90 / 100

print("Final quantities:", quantity)
print("Final bill:", total)
print("Remaining budget:", budget - total)
