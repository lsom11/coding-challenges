class Solution(object):
    def sortArrayByParityII(self, A):
        odds = list()
        evens = list()
        sortedList = list()
        for num in A:
            if num % 2 == 0: evens.append(num)
            else: odds.append(num)
        for i in range(len(A)):
            if i % 2 == 0:
                sortedList.append(evens.pop(0))
            else: sortedList.append(odds.pop(0))
        return sortedList
        