"""class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for i in nums:
            if i not in l:
                l.append(i)
        if len(l)==len(nums):
            return False
        else:
            return True
"""
"""class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        seen=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
        if len(seen)!=len(nums):
            return True
        else:
            return False
"""
class Solution:
    def hasDuplicate(self,nums:List[int])->bool:
        seen=set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
