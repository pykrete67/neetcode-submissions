# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # basically do one pass to get length of linked list first the subtract with n to get the exact index of the node that needs to be removed
        len = 0
        current = head
        while current:
            len += 1
            current = current.next
        print("len:" + str(len))
        # edge case
        if len == 1:
            return None
        index = len - n
        #edge case
        if index == 0:
            return head.next
        print("index:" + str(index))
        count = 1
        currentt = head

        while currentt:
            print(currentt.val)
            if count == index:
                currentt.next = currentt.next.next
                return head
            count += 1
            currentt = currentt.next
        
        return head
        