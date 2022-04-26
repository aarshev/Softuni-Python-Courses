import sys

fruit = input()
day_of_the_week = input()
qnt = float(input())
price = 0.0

if day_of_the_week == "Saturday" or \
   day_of_the_week == "Sunday":
    if fruit == "banana":
        price = 2.7 * qnt
    elif fruit == "apple":
        price = 1.25 * qnt
    elif fruit == "orange":
        price = 0.9 * qnt
    elif fruit == "grapefruit":
        price = 1.6 * qnt
    elif fruit == "kiwi":
        price = 3 * qnt
    elif fruit == "pineapple":
        price = 5.6 * qnt
    elif fruit == "grapes":
        price = 4.2 * qnt
    else:
        print("error")
        sys.exit()
elif day_of_the_week == "Monday" or \
     day_of_the_week == "Tuesday" or \
     day_of_the_week == "Wednesday" or \
     day_of_the_week == "Thursday" or \
     day_of_the_week == "Friday":
    if fruit == "banana":
        price = 2.5 * qnt
    elif fruit == "apple":
        price = 1.2 * qnt
    elif fruit == "orange":
        price = 0.85 * qnt
    elif fruit == "grapefruit":
        price = 1.45 * qnt
    elif fruit == "kiwi":
        price = 2.7 * qnt
    elif fruit == "pineapple":
        price = 5.5 * qnt
    elif fruit == "grapes":
        price = 3.85 * qnt
    else:
        print("error")
        sys.exit()
else:
    print("error")
    sys.exit()

print(f'{price:.2f}')
