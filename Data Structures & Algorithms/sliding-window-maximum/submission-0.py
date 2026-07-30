class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)-k+1):
            max1=float('-inf')
            for j in range(i,i+k):
                max1=max(max1,nums[j])
            l.append(max1)
        return l


        