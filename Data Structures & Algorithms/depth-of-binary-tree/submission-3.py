# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if root==None:
        #     return 0
        # return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

        if not root:
            return 0

        q = deque([root])
        max_depth = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            max_depth += 1
        return max_depth