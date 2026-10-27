items = ["Tea", "Coffee", "Samosa"]
price = [10, 20, 15]
stock = [20, 15, 10]
sales = 0

n = int(input("Enter number of orders: "))

for i in range(n):
    print("1.Tea  2.Coffee  3.Samosa")
    item = int(input("Choose item: ")) - 1
    qty = int(input("Enter quantity: "))

    if item < 0 or item >= 3 or qty <= 0:
        print("Invalid order")
    elif qty > stock[item]:
        print("Not enough stock")
    else:
        bill = price[item] * qty
        stock[item] -= qty
        sales += bill
        print("Bill: Rs.", bill)

print("Total daily sales: Rs.", sales)

for i in range(3):
    print(items[i], "remaining:", stock[i])
