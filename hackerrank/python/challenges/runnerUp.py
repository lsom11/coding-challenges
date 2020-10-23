#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
n = int(input())
arr = map(int, raw_input().split())
arr.sort(reverse=True)
max_num=arr[0]
i=0
while(arr[i]==max_num):
    i+=1
else:
    print(arr[i])
