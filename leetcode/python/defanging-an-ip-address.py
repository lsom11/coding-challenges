class Solution(object):
    def defangIPaddr(self, address):
        print(address)
        return address.replace('.', '[.]')


s = Solution()
s.defangIPaddr("1.1.1.1")  # "1[.]1[.]1[.]1"
