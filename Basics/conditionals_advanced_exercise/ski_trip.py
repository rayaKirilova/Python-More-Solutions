days_count = int(input())
room_type = input()
feedback = input()
price_for_stay = 0
nights = days_count - 1

if days_count < 10:
    if room_type == "room for one person":
        price_for_stay = nights * 18
    elif room_type == "apartment":
        price_for_stay = nights * 25
        price_for_stay -= price_for_stay * 0.3
    elif room_type == "president apartment":
        price_for_stay = nights * 35
        price_for_stay -= price_for_stay * 0.1
elif 10 <= days_count <= 15:
    if room_type == "room for one person":
        price_for_stay = nights * 18
    elif room_type == "apartment":
        price_for_stay = nights * 25
        price_for_stay -= price_for_stay * 0.35
    elif room_type == "president apartment":
        price_for_stay = nights * 35
        price_for_stay -= price_for_stay * 0.15
elif days_count > 15:
    if room_type == "room for one person":
        price_for_stay = nights * 18
    elif room_type == "apartment":
        price_for_stay = nights * 25
        price_for_stay -= price_for_stay * 0.5
    elif room_type == "president apartment":
        price_for_stay = nights * 35
        price_for_stay -= price_for_stay * 0.2

if feedback == "positive":
    price_for_stay += price_for_stay * 0.25
elif feedback == "negative":
    price_for_stay -= price_for_stay * 0.1

print(f'{price_for_stay:.2f}')
