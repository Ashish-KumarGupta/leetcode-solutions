# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def helper(self, node, ans):
            if node == None:
                return
            ans.append(node.val)
            self.helper(node.left,ans)
            self.helper(node.right,ans)
        
    def preorderTraversal(self, root):
        ans = []
        self.helper(root,ans)
        return ans

        
        