# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(preorder)<1:
            return None
        root_val = preorder[0]
        root = TreeNode(val=root_val)
        m = 0
        while inorder[m]!=root_val:
            m += 1
        root.left = self.buildTree(preorder[1:1+m], inorder[:m])
        root.right = self.buildTree(preorder[1+m:], inorder[1+m:])
        return root
        
        