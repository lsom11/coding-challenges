from collections import Counter


def palindrome_permutation(s):
    parsed_str = ''.join(s.split(' ')).lower()
    if (len(parsed_str)) == 1:
        print(True)
    c = Counter(parsed_str)
    if len(parsed_str) % 2 == 0:
        print(all(item % 2 == 0 for item in list(c.values())))
    else:
        for char in parsed_str:
            if c[char]:
                c[char] -= 1
            if c[char] == 0:
                del c[char]
        print(all(item == 1 for item in list(c.values())))


palindrome_permutation('tact coa')
palindrome_permutation('test')
palindrome_permutation('tsssst')
