count = int(input())
total_count = 0

first_group = 0
second_group = 0
third_group = 0
fourth_group = 0
fifth_group = 0

for _ in range(count):
    group_count = int(input())
    total_count += group_count

    if group_count <= 5:
        first_group += group_count
    elif 6 <= group_count <= 12:
        second_group += group_count
    elif 13 <= group_count <= 25:
        third_group += group_count
    elif 26 <= group_count <= 40:
        fourth_group += group_count
    elif group_count >= 41:
        fifth_group += group_count

first_group_percent = first_group / total_count * 100
second_group_percent = second_group / total_count * 100
third_group_percent = third_group / total_count * 100
fourth_group_percent = fourth_group / total_count * 100
fifth_group_percent = fifth_group / total_count * 100

print(f'{first_group_percent:.2f}%')
print(f'{second_group_percent:.2f}%')
print(f'{third_group_percent:.2f}%')
print(f'{fourth_group_percent:.2f}%')
print(f'{fifth_group_percent:.2f}%')

