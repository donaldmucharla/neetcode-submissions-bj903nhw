# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q =collections.deque([root])

        while q:
            rightnode = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightnode = node
                    q.append(node.left)
                    q.append(node.right)
            if rightnode:
                res.append(rightnode.val)
        
        return res
        