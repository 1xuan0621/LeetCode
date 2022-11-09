class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        l = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[l]:
                l = i
                continue
            profit = max(profit, prices[i] - prices[l])
        return profit

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))