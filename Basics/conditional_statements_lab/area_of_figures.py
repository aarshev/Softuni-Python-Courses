import math
figure = input()

area = 0.0
if figure == "square":
    side = float(input())
    area = math.pow(side, 2)
elif figure == "rectangle":
    side = float(input())
    side2 = float(input())
    area = side * side2
elif figure == "circle":
    r = float(input())
    area = math.pi * math.pow(r, 2)
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f'{area:.3f}')

