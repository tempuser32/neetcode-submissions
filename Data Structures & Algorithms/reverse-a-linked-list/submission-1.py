# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        while cur:
            next1=cur.next
            cur.next=prev
            prev=cur
            cur=next1
        return prev
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        l=[]
        while cur:
            val=cur.val
            l.append(val)
            cur=cur.next
        l=l[::-1]
        newhead=None
        newtail=None
        for i in l:
            a=ListNode(i)
            if newhead is None:
                newhead=a
                newtail=a
            else:
                newtail.next=a
                newtail=a
        return newhead            

        
        