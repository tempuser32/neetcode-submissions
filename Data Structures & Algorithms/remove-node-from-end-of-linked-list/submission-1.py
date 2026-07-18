# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        len1=0
        while cur:
            len1+=1
            cur=cur.next
        remove=len1-n
        print(remove)
        if remove==0:
            return head.next
        cur=head
        count=0
        while cur and count!=remove-1:
            cur=cur.next
            count+=1
        cur.next=cur.next.next
        return head
"""    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=fast=head
        for i in range(0,n):
            fast=fast.next
        if fast is None:
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head