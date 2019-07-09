def disemvowel(string):
    filteredString = []
    vowels = ['A', 'E', 'I', 'O', 'U']
    for char in string:
      if not char.upper() in vowels:
        filteredString.append(char)
    return ''.join(filteredString)