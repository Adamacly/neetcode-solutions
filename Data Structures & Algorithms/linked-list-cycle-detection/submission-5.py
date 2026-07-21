# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # a = head
        # length = 0
        # nodes = []
        # while a != None:
        #     if a in nodes:
        #         return True
        #     nodes.append(a)
        #     a = a.next
        # return False

        slow = head
        fast = head
        if slow == None:
            return False

        while slow.next and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

        