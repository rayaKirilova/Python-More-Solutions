jury_count = int(input())
command = input()
sum_grades_by_presentation = 0
total_grades_sum = 0
counter = 0

while command != "Finish":
    presentation_name = command
    for _ in range(jury_count):
        grade = float(input())
        sum_grades_by_presentation += grade
        total_grades_sum += grade

    counter += jury_count
    avg_grade = sum_grades_by_presentation / jury_count
    print(f'{presentation_name} - {avg_grade:.2f}.')
    sum_grades_by_presentation = 0
    command = input()

avg_grade_from_all_presentations = total_grades_sum / counter
print(f'Student\'s final assessment is {avg_grade_from_all_presentations:.2f}.')

