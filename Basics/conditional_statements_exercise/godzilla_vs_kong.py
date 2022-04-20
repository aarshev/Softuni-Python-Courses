budget = float(input())
count_personal = int(input())
price_per_cloth = float(input())

price_all_clothes = count_personal * price_per_cloth

if count_personal > 150:
    price_all_clothes *= 0.9

scene_price = budget * 0.1

budget = budget - price_all_clothes - scene_price

if budget < 0:
    print("Not enough money!")
    print(f"Wingard needs {abs(budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {abs(budget):.2f} leva left.")