from collections import Counter
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




        