"""class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        
        for i in nums:
            newsubset=[]
            for subset in res:
                new=subset+[i]
                newsubset.append(new)
            res.extend(newsubset)
        return res
"""

class Solution:
    def subsets(self,nums:List[int])->List[List[int]]:
        res=[]
        subset=[]
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res


        