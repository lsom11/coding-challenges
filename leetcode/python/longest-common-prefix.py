class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or '' in strs:
            return ''
        
        lens = [len(str) for str in strs]
        min_len, res = min(lens), ''

        for i in range(min_len):
            prefix = strs[0][:i + 1]
            for s in strs:             
                # if the string isnt equal to the prefix 
                # we break and return otherwise we set it to the prefix and go to next str
                if s[:i + 1] != prefix:
                    return res
            res = prefix

        return res