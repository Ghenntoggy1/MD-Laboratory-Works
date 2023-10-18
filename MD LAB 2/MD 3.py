# 3. Check Password
pas = input("Input Password for Check: ")
check_lower = 0
check_upper = 0
check_digit = 0
check_special = 0
special_chars = "~`!@#$%^&*()-_+={}[]|\\;:\"<>,./?"
for i in pas:
    if i.islower():
        check_lower = 1
    elif i.isupper():
        check_upper = 1
    elif i.isnumeric():
        check_digit = 1
    elif i in special_chars:
        check_special = 1
steps = 4 - check_lower - check_upper - check_digit - check_special
reps = 0
for i in range(0, len(pas) - 2, 3):
    # print(pas[i-2], pas[i-1], pas[i])
    # print(pas[i - 1], pas[i], pas[i+1])
    # print(pas[i], pas[i + 1], pas[i + 2])
    if (i != 0) and (i < len(pas) - 2) and (pas[i] == pas[i + 1] == pas[i + 2] or pas[i - 2] == pas[i - 1] == pas[i] or pas[i - 1] == pas[i] == pas[i + 1]):
        reps += 1
    elif (i == 0) and (len(pas) > 2) and (pas[i] == pas[i + 1] == pas[i + 2]):
        reps += 1
    elif (i == len(pas) - 2) and (pas[i - 1] == pas[i] == pas[i + 1]):
        reps += 1
    elif (i == len(pas) - 1) and (pas[i - 2] == pas[i - 1] == pas[i]):
        reps += 1
if reps > 6:
    reps = 6
if reps > steps:
    steps = reps
if steps <= 8 - len(pas):
    steps = 8 - len(pas)
elif len(pas) > 20:
    steps = len(pas) - 20 + steps
if steps == 0:
    print("Good!")
elif steps != 0:
    print("Steps Needed for Good Password:", steps)
