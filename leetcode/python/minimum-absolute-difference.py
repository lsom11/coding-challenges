import sys

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        minimum_absolute_diff = sys.maxsize
        pairs = list()
        
        for i in range(len(arr) - 1):
            current_absolute_diff = abs(arr[i] - arr[i + 1])
            if (current_absolute_diff < minimum_absolute_diff):
                pairs = [[arr[i], arr[i + 1]]]
                
            elif (current_absolute_diff == minimum_absolute_diff):
                pairs.append([arr[i], arr[i + 1]])
                
                
            minimum_absolute_diff = min(minimum_absolute_diff, current_absolute_diff)
            
        return pairs
        