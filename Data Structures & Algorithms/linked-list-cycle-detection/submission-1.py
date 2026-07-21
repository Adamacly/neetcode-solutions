# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a = head
        length = 0
        nodes = []
        while a != None:
            if a in nodes:
                return True
            nodes.append(a)
            a = a.next
        return False

        