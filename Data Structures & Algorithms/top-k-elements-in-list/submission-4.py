"""from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=dict(Counter(nums))
        l=[]
        for i in a:
            l.append((i,a[i]))
        l=sorted(l,key=lambda l:l[1])
        new=[]
        n=-1
        for i in range(0,k):
            new.append(l[n][0])
            n-=1
        return new
"""
"""
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)
        

        for i in count:
            heapq.heappush(heap,(count[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for i in nums:
            count[i]=1+count.get(i,0)

        freq=[[] for i in range(len(nums)+1)]

        for num,amt in count.items():
            freq[amt].append(num)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res





        