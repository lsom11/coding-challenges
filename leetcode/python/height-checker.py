class Solution(object):
    def heightChecker(self, h):
        count = 0
        
        # create an iterator; normal array and array sorted
        comparables = zip(h, sorted(h))

        # map through arrays, checking if values are the same or not, adding to sum if so
        for comparable in comparables:
            a, b = comparable
            if a != b: count += 1
        
        return count