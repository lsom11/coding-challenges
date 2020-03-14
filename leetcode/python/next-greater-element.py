class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []

        stack = [nums2[0]]
        hash = {}

        for i in nums2[1:]:

            while stack and i > stack[-1]:
                hash[stack[-1]] = i
                stack.pop()

            stack.append(i)

        for j in stack:
            hash[j] = -1

        return [ hash[k] for k in nums1 ]
