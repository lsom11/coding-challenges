N = int(input())
english_subs = set(map(int, input().split()))

M = int(input())
french_subs = set(map(int, input().split()))

print(len(english_subs.difference(french_subs)))
