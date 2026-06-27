class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0

        for price in prices[1:]:
            profit = max(profit, price - minimum)
            minimum = min(minimum, price)
        return profit