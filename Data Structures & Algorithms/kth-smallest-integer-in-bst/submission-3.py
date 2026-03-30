class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root
        while True:
            # go left as far as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            # visit node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            # go right
            curr = curr.right
