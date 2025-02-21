import math

tournament_count = int(input())
start_points = int(input())
final_points = start_points

winner_count = 0

for _ in range(tournament_count):
    tournament_result = input()

    if tournament_result == 'W':
        winner_count += 1
        final_points += 2000
    elif tournament_result == 'F':
        final_points += 1200
    elif tournament_result == 'SF':
        final_points += 720

final_points = math.floor(float(final_points))
average_points = math.floor((final_points - start_points) / tournament_count)
winning_percent = winner_count / tournament_count * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{winning_percent:.2f}%')