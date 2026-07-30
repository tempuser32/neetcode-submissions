"""class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(0,len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
            res=max(res,len(seen))
        return res
"""
"""
class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        l=0
        res=0
        seen=set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res=max(res,r-l+1)
        return res
"""
class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        res=0
        ind={}
        for i in range(len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                res=max(res,len(seen))
                ind[j-i+1]=(i,j)
        if len(s)>0:
            a=max(ind)
            b=ind[a]
            print(b)
            print(s[b[0]:b[1]+1])
        return res

        