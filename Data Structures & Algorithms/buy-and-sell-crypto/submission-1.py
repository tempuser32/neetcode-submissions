"""class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                profit=prices[j]-prices[i]
                maxp=max(maxp,profit)
        return maxp
"""
class Solution:
    def maxProfit(self,prices:List[int])->int:
        left=0
        right=1
        maxp=0
        while right < len(prices):
            if prices[right]<prices[left]:
                left=right
            else:
                profit=prices[right]-prices[left]
                maxp=max(maxp,profit)
            right+=1
        return maxp
        