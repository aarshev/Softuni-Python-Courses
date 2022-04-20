hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
minutes_plus_15 = minutes + hours_to_minutes + 15

final_hours = minutes_plus_15 // 60
final_minutes = minutes_plus_15 % 60

if final_hours > 23:
    final_hours = final_hours % 24

if final_minutes < 10:
    print(f'{final_hours}:0{final_minutes}')
else:
    print(f'{final_hours}:{final_minutes}')
