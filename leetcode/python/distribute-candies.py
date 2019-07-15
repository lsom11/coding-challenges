class Solution:
    def distributeCandies(self, candies):
      return min(len(candies)>>1, len(set(candies)))