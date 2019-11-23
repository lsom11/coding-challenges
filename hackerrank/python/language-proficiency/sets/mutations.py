A = int(input())
s = set(map(int, input().split(' ')))
number_of_sets = int(input())

for _ in range(number_of_sets):
    command = input().split(' ')
    new_set = set(map(int, input().split(' ')))
    if command[0] == 'intersection_update':
        s.intersection_update(new_set)
    elif command[0] == 'symmetric_difference_update':
        s.symmetric_difference_update(new_set)
    elif command[0] == 'difference_update':
        s.difference_update(new_set)
    else:
        s.update(new_set)

print(sum(s))
