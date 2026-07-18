# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        cur=head
        while cur not in visited and cur:
            visited.add(cur)
            cur=cur.next
        if cur is None:
            return False
        else:
            return True


        