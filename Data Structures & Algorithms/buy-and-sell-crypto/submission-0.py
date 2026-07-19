class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        for k in range(len(prices)):
            for i in range(k+1, len(prices)):
                profits.append(prices[i] - prices[k])
        return max(profits)
        