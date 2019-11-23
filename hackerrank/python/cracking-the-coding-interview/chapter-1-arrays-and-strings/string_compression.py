import unittest


def string_compression(s):
    l = list()
    temp_char = ''
    count = 0

    for char in s:
        if char == temp_char:
            count += 1
        else:
            if temp_char != '':
                l.append(temp_char + str(count))
            temp_char = char
            count = 1
    l.append(temp_char + str(count))

    compressed = ''.join(l)
    if len(compressed) > len(s):
        print(s)
        return(s)
    else:
        print(''.join(l))
        return(''.join(l))


class TestStringCompression(unittest.TestCase):
    def setUp(self):
        pass

    def test_string_compression(self):
        self.assertEqual(string_compression('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(string_compression('abcccdeab'), 'abcccdeab')


if __name__ == '__main__':
    unittest.main()
