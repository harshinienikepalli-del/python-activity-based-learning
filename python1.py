held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))

if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance details")
else:
    percentage = attended / held * 100
    print("Current attendance:", round(percentage, 2), "%")

    extra = 0

    while percentage < 75:
        held += 1
        attended += 1
        extra += 1
        percentage = attended / held * 100

    if extra == 0:
        print("You already meet the 75% requirement.")
    else:
        print("Minimum consecutive classes to attend:", extra)

    print("Attendance after those classes:",
          round(percentage, 2), "%")
