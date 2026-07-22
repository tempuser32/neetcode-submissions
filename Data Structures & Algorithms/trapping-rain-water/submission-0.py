class Solution:
    def trap(self, height: List[int]) -> int:
        l=[0]*len(height)
        for i in range(len(height)):
            left=max(height[:i+1])
            right=max(height[i:])
            water=min(left,right)-height[i]
            l[i]=(water)
        return sum(l)
        