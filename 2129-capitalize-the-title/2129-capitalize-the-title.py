class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res=""
        for i in title.split(" "):
            if len(i)<3:
                i=i.lower()
            else:
                i=i.capitalize()
            res+=i+" "
        return res.rstrip()