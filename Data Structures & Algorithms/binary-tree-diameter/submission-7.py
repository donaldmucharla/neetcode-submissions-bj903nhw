# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0
            
            # Recursively find the height of left and right subtrees
            left = dfs(curr.left)
            right = dfs(curr.right)

            # Update the global maximum diameter
            # Diameter at this node = left height + right height
            self.res = max(self.res, left + right)

            # Return the height of the current node to its parent
            return 1 + max(left, right)

        dfs(root)
        return self.res