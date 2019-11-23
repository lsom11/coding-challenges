N = int(input())
countries = set()

for i in range(N):
    country = input()
    if not country in countries:
        countries.add(country)

print(len(countries))
