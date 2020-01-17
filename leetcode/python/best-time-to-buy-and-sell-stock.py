class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            profit = - float('inf')
            min_so_far = prices[0]
            for idx in range(1, len(prices)):
                price = prices[idx]
                if price < min_so_far:
                    min_so_far = price
                elif price > min_so_far:
                    profit = max(price-min_so_far, profit)
            return profit if profit > 0 else 0
        return 0
