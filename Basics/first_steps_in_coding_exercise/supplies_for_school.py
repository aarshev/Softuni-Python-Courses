pens = int(input())
markers = int(input())
liters_cleaning = int(input())
discount_percent = int(input())

sum = (pens * 5.8 + markers * 7.2 + liters_cleaning * 1.2) * ((100 - discount_percent) / 100)
print(sum)

