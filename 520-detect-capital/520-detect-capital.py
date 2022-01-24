class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capt=word.capitalize()
        upc=word.upper()
        lwc=word.lower()
        if word == capt or word == upc or word == lwc:
            return True