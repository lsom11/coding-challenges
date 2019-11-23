import re


regex_pattern = r"^[7-9]\d{9}$"
test_cases = int(input())

for _ in range(test_cases):
    string = str(input())
    print("YES" if re.match(regex_pattern, string) else "NO")
