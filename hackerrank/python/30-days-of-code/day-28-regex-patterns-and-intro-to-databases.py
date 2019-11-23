import re


regex = re.compile("^[a-z\.]+@gmail.com$")

accounts = dict()


N = int(input().strip())
for _ in range(N):
    firstName, email = input().strip().split(' ')
    if regex.match(email):
        accounts[email] = firstName

sorted_names = sorted(accounts.values())
print(*sorted_names, sep="\n")
