class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s,m=0,-10001
        for i in nums:
            s+=i
            if s>m:
                m=s
            if s<0:
                s=0
        return m