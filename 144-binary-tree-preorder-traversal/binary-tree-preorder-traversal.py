# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        ans = []

        def helper(node):
            if node == None:
                return
            ans.append(node.val)
            helper(node.left)
            helper(node.right)
        helper(root)
        return ans
        