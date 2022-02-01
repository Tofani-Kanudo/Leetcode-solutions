class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t,prof=prices[0],0
        for i in prices[1:]:
            if i<t:
                t=i
            elif i-t>prof:
                prof=i-t
        return prof
                