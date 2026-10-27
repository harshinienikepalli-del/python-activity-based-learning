vehicle = input("Enter vehicle type (bike/car/heavy): ")
n = int(input("Enter number of violations: "))

total = 0

for i in range(n):
    print("Violation", i + 1)

    print("1. No helmet")
    print("2. Signal jumping")
    print("3. Overspeeding")

    offence = int(input("Enter offence number: "))
    repeat = input("Is it a repeat offence? (yes/no): ")

    if offence == 1:
        fine = 500
    elif offence == 2:
        fine = 1000
    elif offence == 3:
        fine = 1500
    else:
        fine = 0
        print("Invalid offence")

    if repeat == "yes":
        fine = fine * 2

    if vehicle == "heavy" and fine > 0:
        fine += 500

    print("Fine:", fine)
    total += fine

print("Total penalty:", total)

if n >= 3:
    print("Status: Disqualified")
else:
    print("Status: Not Disqualified")
