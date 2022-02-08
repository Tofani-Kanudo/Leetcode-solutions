class Solution:
    def minimumSum(self, num: int) -> int:
        x=list(str(num))
        x.sort()
        return int(x[0])*10+int(x[2]) + int(x[1])*10+int(x[3])