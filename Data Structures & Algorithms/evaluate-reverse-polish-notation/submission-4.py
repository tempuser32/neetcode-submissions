class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        op={"*","-","+","/"}
        for i in tokens:
            ans=0
            if i in op:
                if i=="+":
                    a=l.pop()
                    b=l.pop()
                    ans=int(b)+int(a)
                    l.append(ans)
                if i=="-":
                    a=l.pop()
                    b=l.pop()
                    ans=int(b)-int(a)
                    l.append(ans)
                if i=="*":
                    a=l.pop()
                    b=l.pop()
                    ans=int(a)*int(b)
                    l.append(ans)
                if i=="/":
                    a=l.pop()
                    b=l.pop()
                    ans=int(b)/int(a)
                    l.append(int(ans))
            else:
                l.append(int(i))
        return l[0]

