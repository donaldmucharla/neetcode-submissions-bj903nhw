"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        if not node:
            return None

        def dfs(node):
            
            if node in old_to_new:
                return old_to_new[node]
            
            clone = Node(node.val)
            old_to_new[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        dfs(node)
        return old_to_new[node]