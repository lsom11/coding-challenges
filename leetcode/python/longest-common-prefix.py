class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or '' in strs:
            return ''

        # get max possible prefix length
        lens = [len(str) for str in strs]
        min_len, res = min(lens), ''

        for i in range(min_len):
            prefix = strs[0][:i + 1]
            for s in strs:
                if s[:i + 1] != prefix:
                    return res
            res = prefix

        return res