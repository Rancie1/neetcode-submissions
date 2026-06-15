# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        l2 = None
        while slow:
            nxt = slow.next
            slow.next = l2
            l2 = slow
            slow = nxt
        
        l1 = head

        while l1.next and l2.next:
            l1Nxt = l1.next
            l1.next = l2
            l1 = l1Nxt
            l2Nxt = l2.next
            l2.next = l1
            l2 = l2Nxt
        
      


        