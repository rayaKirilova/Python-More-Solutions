import sys

count = int(input())
numbers_sum = 0
max_number = -sys.maxsize

for _ in range(count):
    number = int(input())
    if number > max_number:
        max_number = number
    numbers_sum += number

if max_number == numbers_sum - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(max_number - (numbers_sum - max_number))
    print('No')
    print(f'Diff = {diff}')








