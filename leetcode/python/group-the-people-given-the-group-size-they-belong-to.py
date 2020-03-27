class Solution:
    def chunks(self, l, n):
    # For item i in a range that is a length of l,
        for i in range(0, len(l), n):
            # Create an index range for l of n items:
            yield l[i:i+n]
    
    flatten = lambda l: [item for sublist in l for item in sublist]
        
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = dict()
        for i in range(len(groupSizes)):
            group = groupSizes[i]
            print(group)
            if group in d:
                d[group].append(i)
            else:
                d[group] = [i]
        output_arr = list()
        for key, value in d.items():
            for l in self.chunks(value, key):
                output_arr.append(l)
        return output_arr
