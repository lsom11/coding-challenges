class Solution:
    def titleToNumber(self, s):
        print(s)
        return sum([(ord(T)-ord("A")+1)*26**i for i,T in enumerate(s[::-1])])