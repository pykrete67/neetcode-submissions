# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
          # get middle node
          fast = head
          slow = head
          while fast and fast.next:
               slow = slow.next
               fast = fast.next.next
          # return slow

          # reverse the second half of the linked list
          current = slow
          prev = None

          while current:
               temp = current.next
               current.next = prev
               prev = current
               current = temp
          #return prev

          slow.next = None
          # merge the 2 lists
          dummy = ListNode(0)
          currentt = dummy
          list1 = head
          list2 = prev
          while list1.next or list2.next:
               currentt.next = list1
               list1 = list1.next
               currentt = currentt.next
               currentt.next = list2
               list2 = list2.next
               currentt = currentt.next


          head = dummy.next
        