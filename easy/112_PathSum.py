class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def dfs(node, path_sum, targetSum):
            if not node:
                return False
            path_sum = path_sum + node.val
            if not node.left and not node.right:
                return True if path_sum == targetSum else False
            return dfs(node.left, path_sum, targetSum) or dfs(node.right, path_sum, targetSum)
        return dfs(root, 0, targetSum)