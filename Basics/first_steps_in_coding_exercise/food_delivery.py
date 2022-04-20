count_chicken = int(input())
count_fish = int(input())
count_vege = int(input())

sum_chicken = count_chicken * 10.35
sum_fish = count_fish * 12.4
sum_vege = count_vege * 8.15
sum_desert = (sum_vege + sum_fish + sum_chicken) * 0.2

final_sum = sum_desert + sum_fish + sum_chicken + sum_vege + 2.5
print(final_sum)
