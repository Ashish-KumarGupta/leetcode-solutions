from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, level, root, ans):
        if not root:
            return
        if level == len(ans):
            ans.append([])
        ans[level].append(root.val)

        self.dfs(level+1, root.left, ans)
        self.dfs(level+1, root.right, ans)

    def levelOrder(self, root):

        ans = []
        self.dfs(0, root, ans)
        return ans
        # ans = []
        # if not root:
        #     return ans
        # q = deque()
        # q.append(root)

        # while q:
        #     level = []
        #     for i in range(len(q)):
        #         current = q.popleft()
        #         level.append(current.val)

        #         if current.left:
        #             q.append(current.left)
        #         if current.right:
        #             q.append(current.right)
        #     ans.append(level)
        # return ans



            

        