# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        def helper(node):
            if node == None:
                return
            helper(node.left)
            helper(node.right)
            res.append(node.val)
        helper(root)
        return res
        