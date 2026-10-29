# class Solution:

#     def dfs(self, node, graph, vis, pathVis, check):
#         vis[node] = 1
#         pathVis[node] = 1

#         for neighbour in graph[node]:

#             if vis[neighbour] == 0:

#                 if self.dfs(neighbour, graph, vis, pathVis, check):
#                     check[node] = 0
#                     return True

#             elif pathVis[neighbour] == 1:
#                 check[node] = 0
#                 return True

#         check[node] = 1
#         pathVis[node] = 0

#         return False

#     def eventualSafeNodes(self, graph):
#         n = len(graph)

#         vis = [0] * n
#         pathVis = [0] * n
#         check = [0] * n

#         for i in range(n):
#             if vis[i] == 0:
#                 self.dfs(i, graph, vis, pathVis, check)

#         ans = []

#         for i in range(n):
#             if check[i] == 1:
#                 ans.append(i)

#         return ans



from collections import deque
class Solution(object):
    def eventualSafeNodes(self, graph):
        n = len(graph)
        indegree = [0]*n
        rev = [[] for i in range(n)]

        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)
                indegree[u] += 1

        q = deque()
        safenode = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node = q.popleft()
            safenode.append(node)
            for i in rev[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return sorted(safenode)



        