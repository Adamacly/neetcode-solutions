# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def BST_to_list(node):
        #     if not node:
        #         return []
        #     else:
        #         return BST_to_list(node.left) + [node.val] + BST_to_list(node.right)
        # bst_list = BST_to_list(root)
        # return(bst_list[k-1])

        n = 0
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n==k:
                return cur.val
            cur = cur.right
        

        