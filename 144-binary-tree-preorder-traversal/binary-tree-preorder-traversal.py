# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def preorderTraversal(self, root):
    #     ans = []

    #     def helper(node):
    #         if node == None:
    #             return
    #         ans.append(node.val)
    #         helper(node.left)
    #         helper(node.right)
    #     helper(root)
    #     return ans






    # def helper(self, root, ans):
    #     if root == None:
    #         return
    #     ans.append(root.val)
    #     self.helper(root.left,ans)
    #     self.helper(root.right,ans)
        
    # def preorderTraversal(self, root):
    #     ans = []
    #     self.helper(root,ans)
    #     return ans

    def preorderTraversal(self, root):
        preorder = []
        if not root:
            return preorder
        st = []
        st.append(root)
        while st:
            root = st[-1]
            st.pop()
            preorder.append(root.val)
            if root.right:
                st.append(root.right)
            if root.left:
                st.append(root.left)
        return preorder