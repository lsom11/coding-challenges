if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, h] for i in range(x + 1) for j in range(y + 1)
           for h in range(z + 1) if ((i + j + h) != n)])
