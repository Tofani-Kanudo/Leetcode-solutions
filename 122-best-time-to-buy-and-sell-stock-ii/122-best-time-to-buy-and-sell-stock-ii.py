class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        buy,prof,fi,t=min(prices[1], prices[0]),0,0,0
        for i in prices[1:]:
            if i<t:
                fi+=t-buy
                buy=i
                prof=0
            elif i-buy>prof:
                prof=i-buy
            t=i
        return prof + fi