# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.goodNode = 0
        def dfs(cur, prev):
            if not cur:
                return
            
            if cur.val >= prev:
                self.goodNode += 1
            prev = max(prev, cur.val)
            dfs(cur.left, prev)
            dfs(cur.right, prev)

        
        dfs(root, float("-inf"))
        return self.goodNode
            

        