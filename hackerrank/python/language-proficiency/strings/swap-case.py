
def transform_letter(letter):
    if letter.isupper():
        return letter.lower()
    if letter.islower():
        return letter.upper()
    return letter


def swap_case(s):
    return ''.join(map(transform_letter, s))
