# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # [1, 2, 3, 4] == root = preord[0]
        # [2, 1, 3, 4] = mid = inorder.index(preord[0])
        #left tree will be preorder[1:mid+1] , inorder[:mid]
        #right tree weill be preord[mid+1:] , inorder[mid+1:]
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        