class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        l=[0]*len(heights)
        for i in range(len(heights)-1):
            num=0
            max1=0
            for j in range(i+1,len(heights)):
                if min(heights[i],heights[j])>max1:
                    num+=1

                    max1=max(max1,heights[j])
            l[i]=num
        return l

        