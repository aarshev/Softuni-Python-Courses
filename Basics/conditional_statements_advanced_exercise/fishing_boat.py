budget = int(input())
season = input()
count_fisherman = int(input())

rent = 0.0

if season == "Spring":
    rent = 3000
elif season == "Winter":
    rent = 2600
else:
    rent = 4200

if count_fisherman <= 6:
    rent *= 0.9
elif 7 <= count_fisherman <= 11:
    rent *= 0.85
else:
    rent *= 0.75

if season != "Autumn" and count_fisherman % 2 == 0:
    rent *= 0.95

budget_diff = abs(budget - rent)
if budget < rent:
    print(f'Not enough money! You need {budget_diff:.2f} leva.')
else:
    print(f'Yes! You have {budget_diff:.2f} leva left.')