# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        print(count)
        mid=count//2
        count=0
        cur=head
        while cur and count!=mid:
            count+=1
            cur=cur.next
        head=cur
        return head


        

            

        