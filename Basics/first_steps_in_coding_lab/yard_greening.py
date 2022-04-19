area = float(input())

first_price = area * 7.61
final_price = first_price * 0.82
discount = first_price - final_price

print(f'The final price is : {round(final_price, 2)} lv.')
print(f'The discount is : {round(discount, 2)} lv.')