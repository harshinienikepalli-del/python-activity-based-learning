names = []
total = 0
n = int(input("Enter number of registrations: "))

for i in range(n):
    name = input("Enter name: ")

    if name in names:
        print("Duplicate registration")
    else:
        names.append(name)
        fee = int(input("Enter registration fee: "))
        total += fee

sponsor = int(input("Enter sponsorship amount: "))
expense = int(input("Enter total expenses: "))

balance = total + sponsor - expense

print("Total participants:", len(names))
print("Registration collection:", total)
print("Final balance:", balance)

if balance < 0:
    print("Loss")
else:
    print("Profit or No Loss")
