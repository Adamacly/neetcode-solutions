# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
         a = head
         while a and a.next:
            b = a
            while b.next.next:
                b = b.next
            f = b.next
            b.next = None
            s = a.next
            a.next = f
            f.next = s
            
            a = a.next.next
         
        