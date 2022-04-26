flower = input()
count_flowers = int(input())
budget = int(input())

expenses = 0.0

if flower == "Roses":
    expenses = count_flowers * 5
    if count_flowers > 80:
        expenses *= 0.9
elif flower == "Dahlias":
    expenses = count_flowers * 3.8
    if count_flowers > 90:
        expenses *= 0.85
elif flower == "Tulips":
    expenses = count_flowers * 2.8
    if count_flowers > 80:
        expenses *= 0.85
elif flower == "Narcissus":
    expenses = count_flowers * 3
    if count_flowers < 120:
        expenses *= 1.15
elif flower == "Gladiolus":
    expenses = count_flowers * 2.5
    if count_flowers < 80:
        expenses *= 1.2

if budget < expenses:
    print(f'Not enough money, you need {abs(budget - expenses):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {count_flowers} {flower} and {abs(budget - expenses):.2f} leva left.')