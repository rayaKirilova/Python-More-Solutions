product = input()
city = input()
quantity = float(input())
total_price = 0

if product == 'coffee':
    if city == 'Sofia':
        total_price = quantity * 0.50
    elif city == 'Plovdiv':
        total_price = quantity * 0.40
    elif city == 'Varna':
        total_price = quantity * 0.45
elif product == 'water':
    if city == 'Sofia':
        total_price = quantity * 0.80
    elif city == 'Plovdiv' or city == 'Varna':
        total_price = quantity * 0.70
elif product == 'beer':
    if city == 'Sofia':
        total_price = quantity * 1.20
    elif city == 'Plovdiv':
        total_price = quantity * 1.15
    elif city == 'Varna':
        total_price = quantity * 1.10
elif product == 'sweets':
    if city == 'Sofia':
        total_price = quantity * 1.45
    elif city == 'Plovdiv':
        total_price = quantity * 1.30
    elif city == 'Varna':
        total_price = quantity * 1.35
elif product == 'peanuts':
    if city == 'Sofia':
        total_price = quantity * 1.60
    elif city == 'Plovdiv':
        total_price = quantity * 1.50
    elif city == 'Varna':
        total_price = quantity * 1.55

print(total_price)



