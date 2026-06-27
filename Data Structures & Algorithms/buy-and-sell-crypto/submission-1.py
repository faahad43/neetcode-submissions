class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0

        for idx in range(1,len(prices)):
            current = prices[idx]
            profit = current - minimum if current - minimum > profit else profit
            minimum = current if minimum > current else minimum
        return profit

        