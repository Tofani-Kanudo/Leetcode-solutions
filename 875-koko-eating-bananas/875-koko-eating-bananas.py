class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minb, maxb = 1, 1000000000
        def caneat(pile, kay, aech):
            hours = 0
            for p in pile:
                hours+=p//kay
                if p%kay!=0:
                    hours+=1
            return hours<=aech
        while minb<=maxb:
            mid=(minb+maxb)//2
            if caneat(piles,mid,h):
                maxb=mid-1
            else:
                minb=mid+1
        return minb