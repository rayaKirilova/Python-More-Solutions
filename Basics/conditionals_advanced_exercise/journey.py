budget = float(input())
season = input()
vacation_price = 0
vacation_type = ''
vacation_destination = ''

if budget <= 100:
    vacation_destination = 'Bulgaria'
    if season == 'summer':
        vacation_type = 'Camp'
        vacation_price = budget * 0.3
    elif season == 'winter':
        vacation_type = 'Hotel'
        vacation_price = budget * 0.7
elif budget <= 1000:
    vacation_destination = 'Balkans'
    if season == 'summer':
        vacation_type = 'Camp'
        vacation_price = budget * 0.4
    elif season == 'winter':
        vacation_type = 'Hotel'
        vacation_price = budget * 0.8
elif budget > 1000:
    vacation_destination = 'Europe'
    vacation_type = 'Hotel'
    vacation_price = budget * 0.9

print(f'Somewhere in {vacation_destination}')
print(f'{vacation_type} - {vacation_price:.2f}')