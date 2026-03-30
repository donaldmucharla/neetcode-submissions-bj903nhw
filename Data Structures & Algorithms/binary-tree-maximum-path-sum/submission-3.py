# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def dfs(root):
            if not root:
                return 0
            leftgain = max(dfs(root.left), 0)
            rightgain = max(dfs(root.right), 0)

            through = root.val+leftgain+rightgain
            self.res = max(self.res, through)

            return root.val+max(leftgain, rightgain)
        

        dfs(root)
        return self.res

        