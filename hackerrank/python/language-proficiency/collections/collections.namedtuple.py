
import collections

N = int(input())
Student = collections.namedtuple('Student', input().split())

sum = 0
for i in range(N):
    line = input().split()
    student = Student(*line)
    sum += int(student.MARKS)

print(sum / N)
