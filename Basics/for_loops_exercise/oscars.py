actor_name = input()
academy_points = float(input())
jury_count = int(input())

for _ in range(jury_count):
    jury_name = input()
    jury_points = float(input())

    academy_points += (len(jury_name) * jury_points) / 2

    if academy_points >= 1250.5:
        print(f'Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!')
        break

if academy_points < 1250.5:
    diff = 1250.5 - academy_points
    print(f'Sorry, {actor_name} you need {diff:.1f} more!')
