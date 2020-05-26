class Solution:
    def findMaxLength(self, nums):
      nums = list(accumulate([x * 2 - 1 for x in nums]))
      ind = defaultdict(list)
      ind[0] = [-1,-1]
      for i in range(len(nums)):
        if not ind[nums[i]]:
          ind[nums[i]] = [i,i]
        else:
          ind[nums[i]][1] = i
      
      max_len = 0
      for i in ind:
        max_len = max(max_len,ind[i][1]-ind[i][0])
      return max_len