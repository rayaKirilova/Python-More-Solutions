city = input()
sales = float(input())
commission = 0

if 0 <= sales <= 500:
    if city == 'Sofia':
        commission = sales * 0.05
    elif city == 'Plovdiv':
        commission = sales * 0.055
    elif city == 'Varna':
        commission = sales * 0.045
    else:
        print('error')
elif 500 < sales <= 1000:
    if city == 'Sofia':
        commission = sales * 0.07
    elif city == 'Plovdiv':
        commission = sales * 0.08
    elif city == 'Varna':
        commission = sales * 0.075
    else:
        print('error')
elif 1000 < sales <= 10000:
    if city == 'Sofia':
        commission = sales * 0.08
    elif city == 'Plovdiv':
        commission = sales * 0.12
    elif city == 'Varna':
        commission = sales * 0.1
    else:
        print('error')
elif sales > 10000:
    if city == 'Sofia':
        commission = sales * 0.12
    elif city == 'Plovdiv':
        commission = sales * 0.145
    elif city == 'Varna':
        commission = sales * 0.13
    else:
        print('error')
else:
    print('error')

if commission > 0:
    print(f'{commission:.2f}')