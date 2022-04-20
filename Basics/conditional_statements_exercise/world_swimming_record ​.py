record = float(input())
meters = float(input())
time_for_meter = float(input())

time_for_distance = meters * time_for_meter
decrease = (meters // 15) * 12.5

final_time = time_for_distance + decrease

if final_time < record:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(final_time - record):.2f} seconds slower.')