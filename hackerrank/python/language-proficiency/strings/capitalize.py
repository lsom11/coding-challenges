def solve(string):
    full_name = string.split(' ')
    return ' '.join((word.capitalize() for word in full_name))
