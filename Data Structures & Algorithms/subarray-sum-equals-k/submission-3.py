"""class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum==k:
                    res+=1
        return res
"""
"""class Solution:
    def subarraySum(self,nums:List[int],k:int)->int:
        prefix=[0]
        sum=0
        ans=0
        for i in nums:
            sum+=i
            prefix.append(sum)
        for i in range(1,len(prefix)):
            for j in range(0,i):
                if prefix[i]-prefix[j]==k:
                    ans+=1
        return ans
"""
"""class Solution:
    def subarraySum(self,nums:List[int],k:int)->int:
        prefix=[0]
        res=0
        for i in nums:
            res+=i
            prefix.append(res)
        print(prefix)
        seen={0:1}
        ans=0
        for i in range(1,len(prefix)):
            needed=prefix[i]-k
            
            if needed in seen:
                ans+=seen[needed]
            
            if prefix[i] in seen:
                seen[prefix[i]]+=1
            else:
                seen[prefix[i]]=1
        return ans
"""
class Solution:
    def subarraySum(self,nums:List[int],k:int)->int:
        prefix=[]
        summ=0
        for i in nums:
            summ+=i
            prefix.append(summ)

        ans=0
        seen={}
        for i in range(len(prefix)):
            if prefix[i]==k:
                ans+=1
            needed=prefix[i]-k
            if needed in seen:
                ans+=seen[needed]
            if prefix[i] in seen:
                seen[prefix[i]]+=1
            else:
                seen[prefix[i]]=1
        return ans

        
            
