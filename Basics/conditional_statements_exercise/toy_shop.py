price_vacation = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count
money_made = puzzles_count * 2.6 + dolls_count * 3 + bears_count * 4.1 + minions_count * 8.2 + trucks_count * 2

if toys_count >= 50:
    money_made *= 0.75

money_made *= 0.9

if price_vacation > money_made:
    print(f"Not enough money! {(price_vacation - money_made):.2f} lv needed.")
else:
    print(f"Yes! {abs(price_vacation - money_made):.2f} lv left.")