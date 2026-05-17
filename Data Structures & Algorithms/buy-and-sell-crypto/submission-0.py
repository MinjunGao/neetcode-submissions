class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        slow = fast = 0
        res = 0

        while fast < len(prices):
            buy, sell = prices[slow], prices[fast]
            res = max(res, sell - buy)
            if sell < buy:
                slow = fast
            fast += 1
        
        return res