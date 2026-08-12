# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # trick: we have 2 pointers, one that is fast and one that is slower, it there is a loop, eventually, the fast one will catch up with the slower one
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
        
        
        
        # i came up with the code below myself, but its hardcoded, so cant
        # count = 1000
        # current = head
        
        # while current and count > -1:
        #     current = current.next
        #     count -= 1
        
        # if count < 0:
        #     return True
        # else:
        #     return False
        