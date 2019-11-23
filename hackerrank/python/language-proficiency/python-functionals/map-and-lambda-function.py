def cube(x): return x ** 3


def fibonacci(n):
    list = []
    for i in range(0, n):
        if i == 0:
            list.append(0)
        elif i == 1:
            list.append(1)
        else:
            list.append(list[i-1] + list[i-2])

    return list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
