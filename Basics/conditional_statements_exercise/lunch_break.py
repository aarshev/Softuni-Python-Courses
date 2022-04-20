import math

series_name = input()
episode_length = int(input())
break_length = int(input())

break_length -= break_length * 3 / 8

if break_length < episode_length:
    print(f"You don't have enough time to watch {series_name}, you need {math.ceil(abs(break_length - episode_length))} more minutes.")
else:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(abs(break_length - episode_length))} minutes free time.")