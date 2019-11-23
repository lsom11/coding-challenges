from collections import Counter
import os

# Complete the makeAnagram function below.


def makeAnagram(a, b):
    char_list = list(set(a + b))
    counter_a = Counter(a)
    counter_b = Counter(b)
    count = 0
    for char in char_list:
        count += abs(counter_a[char] - counter_b[char])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
