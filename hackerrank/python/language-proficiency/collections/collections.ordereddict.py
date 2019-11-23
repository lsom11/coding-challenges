from collections import OrderedDict

N = int(input())
d = OrderedDict()


for i in range(N):
    item = input().strip().split()
    item_name = (" ").join(item[0:len(item)-1])
    net_price = int(item[len(item)-1])
    try:
        d[item_name] += net_price
    except KeyError:
        d[item_name] = net_price


for item in d.items():
    print(item[0], item[1])
