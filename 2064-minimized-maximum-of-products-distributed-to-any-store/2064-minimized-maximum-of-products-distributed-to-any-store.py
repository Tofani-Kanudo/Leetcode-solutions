class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        mins,maxs=1, max(quantities)
        def canget(mids, quantity, n):
            return sum((q + mids - 1) // mids for q in quantity) > n
        while mins<maxs:
            mid=(mins+maxs)//2
            if canget(mid,quantities,n):
                mins=mid+1
            else:
                maxs=mid
        return mins