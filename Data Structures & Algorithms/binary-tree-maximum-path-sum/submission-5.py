# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            
            leftmax = dfs(cur.left)
            rightmax = dfs(cur.right)

            leftmax = max(leftmax, 0)
            rightmax = max(rightmax, 0)

            res = max(res, cur.val+leftmax+rightmax)

            return cur.val+max(leftmax, rightmax)

        dfs(root)
        return res
        