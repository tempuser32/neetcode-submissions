'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
'''
class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        seen={}
        for i in range(0,len(nums)):
            x=target-nums[i]
            if x not in seen:
                seen[nums[i]]=i
            else:
                return [seen[x],i]
        return []
