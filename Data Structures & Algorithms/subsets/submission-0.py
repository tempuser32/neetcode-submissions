class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        
        for i in nums:
            newsubset=[]
            for subset in res:
                new=subset+[i]
                newsubset.append(new)
            res.extend(newsubset)
        return res



        