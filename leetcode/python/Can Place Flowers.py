class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        t = [len(list(j)) for i, j in groupby([0] + flowerbed + [0])]
        return sum((i-1)//2 for i in t[0::2]) >= n