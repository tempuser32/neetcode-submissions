class Solution:
    def isana(self,s:str,t:str):
        if sorted(s)==sorted(t):
            return True
        return False
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=[]

        for name in strs:
            group_found=False
            for group in groups:
                if self.isana(name,group[0]):
                    group.append(name)
                    group_found=True
                    break
            if not group_found:
                groups.append([name])
        return groups
