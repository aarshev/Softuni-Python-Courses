l = int(input())
w = int(input())
h = int(input())
percent = int(input())

v_liters = h * w * l * 0.001

liters_requierd = v_liters * ((100 - percent) / 100)

print(liters_requierd)