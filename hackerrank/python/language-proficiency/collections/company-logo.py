import collections

s = input()
counter = collections.Counter(s).most_common()


counter = sorted(counter,  key=lambda x: (x[1] * -1, x[0]))
for i in range(3):
    print(counter[i][0], counter[i][1])
