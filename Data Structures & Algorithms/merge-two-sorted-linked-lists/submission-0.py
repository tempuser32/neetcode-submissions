# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        r=[]
        cur=list1
        while cur:
            l.append(cur.val)
            cur=cur.next
        print(l)
        cur=list2
        while cur:
            r.append(cur.val)
            cur=cur.next
        print(r)
        new=l+r
        new1=sorted(new)
        print(new1) 
        head=tail=None
        for i in new1:
            newnode=ListNode(i)
            if head is None:
                head=newnode
                tail=newnode
            else:
                tail.next=newnode
                tail=newnode
        return head

        