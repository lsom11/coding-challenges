class Solution(object):
    def duplicateZeros(self, arr):
            i, n = 0, len(arr)
            while i < n:
                if arr[i]==0:
                    arr.insert(i,0)
                    arr.pop()
                    i += 2
                else:
                    i += 1