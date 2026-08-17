# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len = 0
        current = head
        while current:
            len += 1
            current = current.next
        print("len:" + str(len))

        if len == 1:
            return None
        index = len - n
        print("index:" + str(index))
        count = 1
        currentt = head

        while currentt and count < len:
            print(currentt.val)
            if count == index:
                currentt.next = currentt.next.next
                return head
            count += 1
            currentt = currentt.next
        
        return head
        