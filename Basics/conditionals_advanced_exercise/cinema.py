type_projection = input()
rows = int(input())
columns = int(input())
cinema_hall_area = rows * columns
total_revenue = 0

if type_projection == 'Premiere':
    total_revenue = cinema_hall_area * 12
elif type_projection == 'Normal':
    total_revenue = cinema_hall_area * 7.50
elif type_projection == 'Discount':
    total_revenue = cinema_hall_area * 5.00

print(f'{total_revenue:.2f} leva')
