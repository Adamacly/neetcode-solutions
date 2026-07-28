# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
            # if not root:
            #     return True
            # if root.left:
            #     left_q = deque([root.left])
            #     while left_q:
            #         node = left_q.popleft()
            #         if node.val >= root.val:
            #             return False
            #         if node.left:
            #             left_q.append(node.left)
            #         if node.right:
            #             left_q.append(node.right)
            # if root.right:
            #     right_q = deque([root.right])
            #     while right_q:
            #         node = right_q.popleft()
            #         if node.val <= root.val:
            #             return False
            #         if node.left:
            #             right_q.append(node.left)
            #         if node.right:
            #             right_q.append(node.right)
            # return self.isValidBST(root.left) and self.isValidBST(root.right)
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val>left and node.val<right):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right) 
        return valid(root, float("-inf"), float("inf"))           