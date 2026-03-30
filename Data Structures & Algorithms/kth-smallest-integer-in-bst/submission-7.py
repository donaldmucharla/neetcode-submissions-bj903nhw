class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # Move to the right subtree
            curr = curr.right