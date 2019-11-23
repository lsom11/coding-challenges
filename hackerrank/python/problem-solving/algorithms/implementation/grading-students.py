#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def get_multiple(x):
    return int(math.ceil(float(x) / 5) * 5)


def gradingStudents(grades):
    new_grades = []
    for grade in grades:
        if grade < 38:
            new_grades.append(grade)
        else:
            next_multiple = get_multiple(grade)
            if abs(grade - next_multiple) < 3:
                new_grades.append(next_multiple)
            else:
                new_grades.append(grade)
    return new_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
