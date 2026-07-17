"""class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l=[0]*len(temperatures)
        for i in range(len(temperatures)-1):
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    l[i]=j-i
                    break
        return l
"""        
class Solution:
    def dailyTemperatures(self,temperatures:List[int])->List[int]:
        answer=[0]*len(temperatures)
        stack=[]
        for i in range(0,len(temperatures)):
            while (stack and temperatures[i]>temperatures[stack[-1]]):
                prev=stack.pop()
                answer[prev]=i-prev
            stack.append(i)
        return answer


        