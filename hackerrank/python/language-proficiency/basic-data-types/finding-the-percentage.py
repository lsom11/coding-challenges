n = int(input())
dict = {}
for _ in range(n):
    student = input()
    student_arr = student.split(' ')
    dict[student[0]] = format(
        (float(student_arr[1]) + float(student_arr[2]) + float(student_arr[3])) / 3, '.2f')

student = input()
print(dict[student[0]])
