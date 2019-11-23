def mutate_string(string, position, character):
    new_string = string[0:position] + character + string[position + 1:]
    return new_string
