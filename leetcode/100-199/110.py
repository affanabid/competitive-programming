# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root) -> bool:
        
        def helperBalanced(node):
            if node is None:
                return [True, 0]  #[balance, height]

            left, right = helperBalanced(node.left), helperBalanced(node.right)

            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1        
            return [balanced, 1 + max(left[1], right[1])]

        return helperBalanced(root)[0]