"""class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1=0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                max1=max(max1,min(heights[j],heights[i])*(j-i))
        return max1
"""
class Solution:
    def maxArea(self,heights:List[int])->int:
        l=0
        r=len(heights)-1
        res=0
        while l<r:
            area=min(heights[r],heights[l])*(r-l)
            res=max(res,area)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res
        