"""class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=sorted(nums)
        return n[len(n)-k]
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]

"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: 
        target=len(nums)-k

        def quickselect(l,r):
            p=l
            pivot=nums[r]
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i],nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]
            if p>target:
                return quickselect(l,p-1)
            elif p<target:
                return quickselect(p+1,r)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)
"""      