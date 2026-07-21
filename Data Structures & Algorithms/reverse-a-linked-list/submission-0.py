# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, nex = None, head
        if head == None:
            return head
        while nex.next != None:   
            l = nex.next
            nex.next = prev
            prev = nex
            nex = l
        nex.next = prev
        return nex
        
        