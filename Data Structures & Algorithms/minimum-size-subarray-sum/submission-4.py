"""class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        seen={}
        for i in range(len(nums)):
            sum1=0
            for j in range(i,len(nums)):
                sum1=sum1+nums[j]
                if sum1>=target:
                    seen[j-i+1]=(i,j)
            print(seen)
        if seen:
            return min(seen)
        else:
            return 0
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen=float('inf')
        for i in range(len(nums)):
            sum1=0
            for j in range(i,len(nums)):
                sum1+=nums[j]
                if sum1>=target:
                    minlen=min(minlen,j-i+1)
                    break
        if minlen!=float('inf'):
            return minlen
        else:
            return 0




        