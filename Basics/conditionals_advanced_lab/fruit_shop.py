product = input()
day = input()
quantity = float(input())
total_price = 0

if product == 'apple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 1.20
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 1.25
    else:
        print('error')
elif product == 'banana':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 2.50
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 2.70
    else:
        print('error')
elif product == 'orange':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 0.85
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 0.90
    else:
        print('error')
elif product == 'grapefruit':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 1.45
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 1.60
    else:
        print('error')
elif product == 'kiwi':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 2.70
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 3.00
    else:
        print('error')
elif product == 'pineapple':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 5.50
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 5.60
    else:
        print('error')
elif product == 'grapes':
    if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
        total_price = quantity * 3.85
    elif day == 'Saturday' or day == 'Sunday':
        total_price = quantity * 4.20
    else:
        print('error')
else:
    print('error')

if total_price > 0:
    print(f'{total_price:.2f}')


