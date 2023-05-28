# # Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.child = 0
#         self.layer = 0

# class binaryTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, val):
#         if self.root == None:
#             self.root = TreeNode(val)
#             self.root.layer += 1
#         else:
#             self._insert(val)

#     def _insert(self, val):
#         saved = 0
#         self.layerList = []
#         curr = self.root
#         currLayer = curr.layer
#         self.layerList.append(curr)
#         while saved == 0:
#             if curr.child == 0:
#                 self.left = TreeNode(val)
#                 self.child += 1
#                 saved += 1
#             elif curr.child == 1:
#                 self.right = TreeNode(val)
#                 self.child += 1
#                 saved += 1
#             elif curr.child == 2:
#                 if currLayer==1:
#                     curr = self.left
#                     self.layerList.append(curr)
#                 else:
#                     pass
            
            


# class Solution:
#     def inorderTraversal(self, root):
#         treeLen = len(root)
#         tree = []
#         for i in range(treeLen):
#             curr = TreeNode(val = root[i])
#             if i<=treeLen/2-1:
#                 curr.left = TreeNode(val = root[i*2+1])
#             if i<treeLen/2-1:
#                 curr.right = TreeNode(val = root[i*2+2])
#             tree.append(curr)

#         return tree
    
# # sol = Solution()
# # inor = sol.inorderTraversal([])

# test = 1

# match test:
#     case 1:
#         print(test)

class Solution:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

class SolutionRecursive:
    def inorderTraversal(self, root):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []
    
sol = Solution()
root = [1,None,2,3]
ino = sol.inorderTraversal(root)
print(ino)