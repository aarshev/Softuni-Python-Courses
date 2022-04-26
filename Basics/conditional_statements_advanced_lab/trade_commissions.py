import sys

city = input()
sales = float(input())

commission = 0.0
if 0 <= sales <= 500:
    if city == "Sofia":
        commission = sales * 0.05
    elif city == "Varna":
        commission = sales * 0.045
    elif city == "Plovdiv":
        commission = sales * 0.055
    else:
        print("error")
        sys.exit()
elif 500 < sales <= 1000:
    if city == "Sofia":
        commission = sales * 0.07
    elif city == "Varna":
        commission = sales * 0.075
    elif city == "Plovdiv":
        commission = sales * 0.08
    else:
        print("error")
        sys.exit()
elif 1000 < sales <= 10000:
    if city == "Sofia":
        commission = sales * 0.08
    elif city == "Varna":
        commission = sales * 0.1
    elif city == "Plovdiv":
        commission = sales * 0.12
    else:
        print("error")
        sys.exit()
elif sales > 10000:
    if city == "Sofia":
        commission = sales * 0.12
    elif city == "Varna":
        commission = sales * 0.13
    elif city == "Plovdiv":
        commission = sales * 0.145
    else:
        print("error")
        sys.exit()
else:
    print("error")
    sys.exit()

print(f'{commission:.2f}')