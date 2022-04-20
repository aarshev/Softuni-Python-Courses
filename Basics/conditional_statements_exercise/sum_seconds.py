time1 = int(input())
time2 = int(input())
time3 = int(input())

time_seconds = time1 + time2 + time3
minutes = time_seconds // 60
seconds = time_seconds % 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')