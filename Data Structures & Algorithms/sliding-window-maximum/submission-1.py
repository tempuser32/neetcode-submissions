"""class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=[]
        for i in range(0,len(nums)-k+1):
            max1=float('-inf')
            for j in range(i,i+k):
                max1=max(max1,nums[j])
            l.append(max1)
        return l
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output=[]
        q=deque()
        l=r=0
        while r<len(nums):
            while q and nums[q[-1]]<nums[r]:
                q.pop()
            q.append(r)

            if l>q[0]:
                q.popleft()
            
            if (r-l+1)==k:
                output.append(nums[q[0]])
                l+=1
            r+=1
        return output


        