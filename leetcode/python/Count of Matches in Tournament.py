numMatches = 0
while n > 1:
    if n % 2 == 0:
        n = n // 2
        numMatches += n
    else:
        n = (n-1) // 2 + 1
        numMatches += n - 1
return numMatches