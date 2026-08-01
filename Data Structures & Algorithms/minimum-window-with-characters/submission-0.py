class Solution:
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