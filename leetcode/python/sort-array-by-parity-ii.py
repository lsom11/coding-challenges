class Solution(object):
    def sortArrayByParityII(self, A):
        odds = list()
        evens = list()
        sortedList = list()
        for num in A:
            if num % 2 == 0: evens.append(num)
            else: odds.append(num)
        for i in range(len(A) / 2):
                sortedList.append(evens[i])
                sortedList.append(odds[i])
        return sortedList
        