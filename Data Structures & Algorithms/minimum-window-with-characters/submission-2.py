"""class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        found=False
        l={}
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if all(s[i:j+1].count(c) >= t.count(c) for c in set(t)):
                    found=True
                    l[len(s[i:j+1])]=(i,j)
        if found==True:
            a=l[min(l)]
            return s[a[0]:a[1]+1]
        else:
            return ""
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        countT={}
        for c in t:
            countT[c]=1+countT.get(c,0)
        need=len(countT)

        window={}
        have=0
        res=[-1,-1]
        l=0
        reslen=float("inf")      

        for r,c in enumerate(s):
            window[c]=1+window.get(c,0)  

            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                if (r-l+1)<reslen:
                    res=[l,r]
                    reslen=r-l+1

                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        if reslen != float('inf'):
            return s[l:r+1]
        else:
            return ""
                
