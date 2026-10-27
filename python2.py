n = int(input("Enter number of subjects: "))

marks = []
grace = 5
total = 0
passed = True

for i in range(n):
    m = int(input("Enter subject marks: "))
    marks.append(m)

for i in range(n):
    if marks[i] < 0 or marks[i] > 100:
        passed = False
        print("Invalid marks")
        break

    if marks[i] < 35:
        needed = 35 - marks[i]

        if needed <= grace:
            marks[i] += needed
            grace -= needed
        else:
            passed = False

    total += marks[i]

if passed:
    percentage = total / (n * 100) * 100

    print("Final marks:", marks)
    print("Percentage:", round(percentage, 2))

    if percentage >= 75:
        print("Result: Distinction")
    elif percentage >= 60:
        print("Result: First Class")
    elif percentage >= 50:
        print("Result: Second Class")
    else:
        print("Result: Pass")
else:
    print("Result: Fail")
