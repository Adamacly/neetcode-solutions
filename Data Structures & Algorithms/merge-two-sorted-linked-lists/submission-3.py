# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        
        a = list1
        b = list2
        res = None
        c = res
        if a.val <= b.val:
            res = a
            c = res
            a = a.next
        else:
            res = b
            c = res
            b = b.next
        while b!=None and a!=None:
            if a.val <= b.val:
                c.next = a
                c = c.next
                a = a.next
            else:
                c.next = b
                c = c.next
                b = b.next

        if b!=None:
            c.next = b
        if a!=None:
            c.next = a
        return res
        