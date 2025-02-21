budget = int(input())
season = input()
fishermen = int(input())
boat_price = 0
discount = 0

if season == 'Summer' or season == 'Autumn':
    boat_price = 4200
elif season == 'Winter':
    boat_price = 2600
elif season == 'Spring':
    boat_price = 3000

if fishermen <= 6:
    discount = 0.1
elif 7 <= fishermen <= 11:
    discount = 0.15
elif fishermen >= 12:
    discount = 0.25

total_boat_price = boat_price - boat_price * discount

if fishermen % 2 == 0 and season != 'Autumn':
    total_boat_price -= total_boat_price * 0.05

diff = abs(budget - total_boat_price)
if budget < total_boat_price:
    print(f'Not enough money! You need {diff:.2f} leva.')
else:
    print(f'Yes! You have {diff:.2f} leva left.')
