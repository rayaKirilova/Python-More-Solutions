age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
toy_count = 0
earn_money = 0
saved_money = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        earn_money += 10
        saved_money += earn_money
    else:
        toy_count += 1

money_taken_by_brother = age // 2
money_from_toys = toy_price * toy_count
total_sum_of_money = (saved_money + money_from_toys) - money_taken_by_brother

diff = abs(total_sum_of_money - washing_machine_price)

if washing_machine_price > total_sum_of_money:
    print(f'No! {diff:.2f}')
else:
    print(f'Yes! {diff:.2f}')
