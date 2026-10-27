n = int(input("Enter number of days: "))

for i in range(n):
    print("Day", i + 1)

    prepared = int(input("Meals prepared: "))
    served = int(input("Meals served: "))
    leftover = int(input("Leftover meals: "))

    if prepared <= 0 or served < 0 or leftover < 0 or served + leftover > prepared:
        print("Invalid details")
    else:
        waste = prepared - served
        percentage = waste / prepared * 100

        print("Wastage:", round(percentage, 2), "%")

        if percentage > 10:
            print("High Wastage")
        else:
            print("Acceptable Wastage")
