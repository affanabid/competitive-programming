# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root) -> int:
        def counter(node):
            if node is None:
                return 0
            l = counter(node.left)
            r = counter(node.right)
            return 1 + l + r
        return counter(root)
    
n = TreeNode(1)
n.left = TreeNode(2)
n.right = TreeNode(3)
n.left.left = TreeNode(4)
n.left.right = TreeNode(5)
n.right.left = TreeNode(6)
n.right.right = TreeNode(7)


sol = Solution()
print(sol.countNodes(n))

