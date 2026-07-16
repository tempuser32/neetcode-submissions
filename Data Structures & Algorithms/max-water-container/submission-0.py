class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1=0
        for i in range(0,len(heights)):
            for j in range(i+1,len(heights)):
                max1=max(max1,min(heights[j],heights[i])*(j-i))
        return max1

        