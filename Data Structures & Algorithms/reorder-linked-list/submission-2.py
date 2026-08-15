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
          while fast.next and fast.next.next:
               slow = slow.next
               fast = fast.next.next
          # return slow
          
          print(slow.val)
          
          # reverse the second half of the linked list
          current = slow.next
          slow.next = None # cut off the ties between first and second list
          prev = None

          while current:
               temp = current.next
               current.next = prev
               prev = current
               current = temp
          #return prev


          # merge the 2 lists
          dummy = ListNode(0)
          currentt = dummy
          list1 = head
          list2 = prev
        #   print(list1.val)
        #   print(list2.val)
          while list1 and list2:
               currentt.next = list1
               list1 = list1.next
               currentt = currentt.next
               currentt.next = list2
               list2 = list2.next
               currentt = currentt.next

          if list1:
            currentt.next = list1
          if list2:
            currentt.next = list2

          head = dummy.next

