class Solution:
    def getLucky(self, s: str, k: int) -> int:
        su=""
        for i in s:
            t=ord(i)-96
            su+=str(t)
        for i in range(k):
            su = str(sum(int(x) for x in su))
        return su