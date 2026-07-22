
"""class Solution:
    def trap(self, height: List[int]) -> int:
        l=[0]*len(height)
        for i in range(len(height)):
            left=max(height[:i+1])
            right=max(height[i:])
            water=min(left,right)-height[i]
            l[i]=(water)
        return sum(l)
"""
"""class Solution:
    def trap(self,height:List[int])->int:
        n=len(height)
        if n==0:
            return 0
        prefix=[0]*n
        suffix=[0]*n  
        prefix[0]=height[0]
        suffix[n-1]=height[n-1]
        for i in range(1,n):
            prefix[i]=max(prefix[i-1],height[i])
        for j in range(n-2,-1,-1):
            suffix[j]=max(suffix[j+1],height[j])
        res=0
        for i in range(n):
            res+=min(prefix[i],suffix[i])-height[i]
        return res
"""
class Solution:
    def trap(self,height:List[int])->int:
        l,r=0,len(height)-1
        leftmax=0
        rightmax=0
        water=0
        while l<=r:
            leftmax=max(leftmax,height[l])
            rightmax=max(rightmax,height[r])
            if leftmax<=rightmax:
                water+=(leftmax-height[l])
                l+=1
            else:
                water+=(rightmax-height[r])
                r-=1
        return water       
