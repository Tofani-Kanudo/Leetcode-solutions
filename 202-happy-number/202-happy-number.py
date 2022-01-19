class Solution:
    def sums(self, nu):
        ans,t=0,0
        while nu:
            t=nu%10
            ans+=t**2
            nu//=10
        return ans
    
    def isHappy(self, n: int) -> bool:
        slow,fast,s=n,n,0
        while fast!=slow or s==0:
            s=1
            slow=self.sums(slow)
            fast=self.sums(fast)
            fast=self.sums(fast)
        if fast==1:
            return "true"
        