class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left= None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)

            if ldepth > rdepth:
                return ldepth + 1
            else:
                return rdepth + 1

root = TreeNode(5)

root.right = TreeNode(3)
root.left = TreeNode(7)

root.right.right = TreeNode(8)
root.right.left = TreeNode(10)
root.left.right = TreeNode(11)
root.left.left = TreeNode(15)

root.left.left.left = TreeNode(20)

root.left.left.left.right = TreeNode(21)

print(Solution().maxDepth(root))
