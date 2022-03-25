class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        r=nums.index(max(nums))
        if nums.pop(r)>=max(nums)*2:
            return r
        return -1