screening = input()
rows = int(input())
cols = int(input())

income = 0.0
seats = rows * cols

if screening == "Premiere":
    income = seats * 12
elif screening == "Normal":
    income = seats * 7.5
else:
    income = seats * 5

print(f'{income:.2f}')