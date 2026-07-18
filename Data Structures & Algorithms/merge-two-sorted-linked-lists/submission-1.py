# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
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
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val>=list2.val:
            head=list2
            list2=list2.next
        else:
            head=list1
            list1=list1.next
        tail=head
        while list1 and list2:
            if list1.val>=list2.val:
                tail.next=list2
                list2=list2.next
            else:
                tail.next=list1
                list1=list1.next
            tail=tail.next
        if list1:
            tail.next=list1
        else:
            tail.next=list2
        return head
                

        