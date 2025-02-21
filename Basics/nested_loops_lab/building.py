floor = int(input())
rooms = int(input())
type_room = ''

for i in range (floor, 0, -1):
    for z in range (0, rooms):
        if i == floor:
            type_room = 'L'
        elif i % 2 == 0:
            type_room = 'O'
        else:
            type_room = 'A'

        print(f'{type_room}{i}{z}', end = " ")
    print()

