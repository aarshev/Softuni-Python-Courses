budget = float(input())
videos_count = int(input())
cpu_count = int(input())
ram_count = int(input())

video_price = videos_count * 250
cpu_price = video_price * 0.35 * cpu_count
ram_price = video_price * 0.1 * ram_count

sum = video_price + cpu_price + ram_price

if videos_count > cpu_count:
    sum *= 0.85

if budget < sum:
    print(f'Not enough money! You need {abs(budget - sum):.2f} leva more!')
else:
    print(f'You have {abs(budget - sum):.2f} leva left!')