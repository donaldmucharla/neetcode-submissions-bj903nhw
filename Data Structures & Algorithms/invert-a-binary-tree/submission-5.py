# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if the node is null, we've reached the end of a branch
        if not root:
            return None
        
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively call the function on the children
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # Return the root after inversion is complete
        return root