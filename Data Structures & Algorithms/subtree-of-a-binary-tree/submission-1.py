# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root == subRoot:
        #     return True
        # elif root==None:
        #     return False
        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        def isSameTree(t, s):
            if not t and not s:
                return True
            elif not t or not s or t.val != s.val:
                return False
            else:
                return isSameTree(t.left, s.left) and isSameTree(t.right, s.right)
        
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if isSameTree(node, subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return False
        