pages = int(input())
pages_per_hour = int(input())
days = int(input())

hours_whole_book = pages // pages_per_hour
hours_per_day = hours_whole_book // days

print(hours_per_day)