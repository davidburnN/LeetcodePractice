class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        path_list = []
        def dfs(node, path_list, path, path_sum, targetSum):
            if not node:
                return 
            new_path = path.copy()
            new_path.append(node.val)
            path_sum += node.val
            if not node.left and not node.right:
                if path_sum == targetSum:
                    path_list.append(new_path)
                return 
            dfs(node.left, path_list, new_path, path_sum, targetSum)
            dfs(node.right, path_list, new_path, path_sum, targetSum)
            return
        dfs(root, path_list, [], 0, targetSum)
        return path_list