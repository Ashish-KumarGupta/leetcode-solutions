# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):

        def dfs(node, path):
            if not node:
                return

            path += str(node.val)

            if not node.left and not node.right:
                result.append(path)
                return
            
            if node.left:
                dfs(node.left, path + "->")
            if node.right:
                dfs(node.right, path + "->")

        result = []
        if root:
            dfs(root, "")
        return result
