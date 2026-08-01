class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=sorted(nums)
        return n[len(n)-k]
        