class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap_stock=float('inf')
        max_profit=0
        for i in range(len(prices)):
            if(cheap_stock<prices[i]):
                max_profit=max(max_profit, prices[i]-cheap_stock)
            else:
                cheap_stock=min(cheap_stock, prices[i])
        return max_profit