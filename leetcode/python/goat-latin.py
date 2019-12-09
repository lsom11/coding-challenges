class Solution(object):
    def toGoatLatin(self, S):
        res, temp = [], ""
        for idx, word in enumerate(S.split()):
            if word[0].lower() not in 'aeiou':
                temp = word[1:]+word[0]
            else:
                temp = word
            res.append(temp + "ma" + "a" * (idx+1))
        return " ".join(res)