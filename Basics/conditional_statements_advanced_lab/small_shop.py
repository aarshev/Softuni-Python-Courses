product = input()
city = input()
qnt = float(input())
price = 0;

if city == "Sofia":
    if product == "coffee":
        price = qnt * 0.5
    elif product == "water":
        price = qnt * 0.8
    elif product == "beer":
        price = qnt * 1.2
    elif product == "sweets":
        price = qnt * 1.45
    else:
        price = qnt * 1.6
elif city == "Plovdiv":
    if product == "coffee":
        price = qnt * 0.4
    elif product == "water":
        price = qnt * 0.7
    elif product == "beer":
        price = qnt * 1.15
    elif product == "sweets":
        price = qnt * 1.30
    else:
        price = qnt * 1.5
else:
    if product == "coffee":
        price = qnt * 0.45
    elif product == "water":
        price = qnt * 0.7
    elif product == "beer":
        price = qnt * 1.1
    elif product == "sweets":
        price = qnt * 1.35
    else:
        price = qnt * 1.55

print(price)