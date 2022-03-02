class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        d=0
        if len(s)==0:
            return True
        for i in range(len(t)):
            if s[d]==t[i]:
                d+=1
                if d==len(s):
                    return True
                