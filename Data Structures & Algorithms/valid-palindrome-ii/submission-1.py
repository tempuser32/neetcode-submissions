"""class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s==s[::-1]:
            return True
        for i in range(0,len(s)):
            newS=s[:i]+s[i+1:]
            if newS==newS[::-1]:
                return True
        return False
"""
class Solution:
    def validPalindrome(self,s:str)->bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skipL=s[l+1:r+1]
                skipR=s[l:r]
                return skipL==skipL[::-1] or skipR==skipR[::-1]
            l+=1
            r-=1
        return True