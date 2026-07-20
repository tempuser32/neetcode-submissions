class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        cur=[]
        def dfs(start,remaining):
            if remaining==0:
                res.append(cur.copy())
                return
            if remaining<0 or start>=len(nums):
                return
            cur.append(nums[start])
            dfs(start,remaining-nums[start])
            cur.pop()
            dfs(start+1,remaining)
        dfs(0,target)
        return res

        