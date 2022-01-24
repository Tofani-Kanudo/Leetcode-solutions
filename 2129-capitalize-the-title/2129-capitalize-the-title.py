class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res=""
        for i in title.split(" "):
            i=i.lower()
            if len(i)>2:
                i=i.capitalize()
            res+=i+" "
        return res.rstrip()