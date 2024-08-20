# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        res = []
        def traverse(node, res):
            if node:
                traverse(node.left, res)
                res.append(node.val)
                traverse(node.right, res)
        traverse(root, res)
        return res