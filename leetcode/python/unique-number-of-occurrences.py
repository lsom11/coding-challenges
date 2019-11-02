class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = dict()
        occurrences_values = list()
        for num in arr:
            if num in occurrences.keys():
                occurrences[num] += 1
            else:
                occurrences[num] = 1
        
        for val in occurrences.values():
            if val in occurrences_values:
                return False
            else: occurrences_values.append(val)
        return True
        