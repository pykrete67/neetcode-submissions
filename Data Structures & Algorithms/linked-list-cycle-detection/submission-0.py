# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        count = 1000
        current = head
        
        while current and count > -1:
            current = current.next
            count -= 1
        
        if count < 0:
            return True
        else:
            return False
        