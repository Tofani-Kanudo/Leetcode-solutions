class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        for i in sorted(accounts, key=lambda x: sum(x), reverse=True):
            return sum(i)