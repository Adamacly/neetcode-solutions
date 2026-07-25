# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []
        if root == None:
            return ans
        while q:
            sublist = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    sublist.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            ans.append(sublist)
        return ans


        