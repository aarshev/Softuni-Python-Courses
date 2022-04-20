nailon = int(input())
paint = int(input())
liters = int(input())
hours = int(input())

sum_nailon = (nailon + 2) * 1.5
sum_paint = (paint * 1.1) * 14.5
sum_liters = liters * 5
sum_work = (sum_nailon + sum_paint + sum_liters  + 0.4) * 0.3 * hours

sum = sum_nailon + sum_paint + sum_liters + sum_work + 0.4
print(sum)