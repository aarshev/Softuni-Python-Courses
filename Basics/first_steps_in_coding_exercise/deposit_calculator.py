money = float(input())
months = int(input())
lihven_procent = float(input())

natrupana_lihwa = money * lihven_procent / 100
lihva_mesec = natrupana_lihwa / 12
sum = money + months * lihva_mesec

print(sum)