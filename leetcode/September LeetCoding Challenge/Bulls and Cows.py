class Solution:
    def getHint(self, secret, guess):
        B = sum([x==y for x,y in zip(secret, guess)])
		Count_sec = Counter(secret)
        Count_gue = Counter(guess)
        B_C = sum([min(Count_sec[elem], Count_gue[elem]) for elem in Count_sec])
        return str(B) + "A" + str(B_C-B) + "B"