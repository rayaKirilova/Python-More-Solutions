start = int(input())
end = int(input())
magic_number = int(input())
counter_combinations = 0
is_found = False

for i in range(start, end+1):
    for j in range(start, end+1):
        sum_nums = i + j
        counter_combinations  += 1
        if sum_nums == magic_number:
            print(f'Combination N:{counter_combinations} ({i} + {j} = {magic_number})')
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f'{counter_combinations} combinations - neither equals {magic_number}')

