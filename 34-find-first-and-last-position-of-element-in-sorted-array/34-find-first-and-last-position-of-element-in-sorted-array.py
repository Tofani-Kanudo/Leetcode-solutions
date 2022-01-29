class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        def t_left(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return l if nums[l] == target else -1

        def t_right(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                m = (l + r) // 2 + 1
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m
            return l if nums[l] == target else -1

        return [t_left(nums, target), t_right(nums, target)]