class Solution(object):
    def dfs(self, node, initcolor, color, graph):
        color[node] = initcolor
        for neighbour in graph[node]:
            if color[neighbour] == -1:
                if self.dfs(neighbour, 1 - initcolor, color, graph) == False:
                    return False
            elif color[neighbour] == initcolor:
                return False
        return True
    def isBipartite(self, graph):
        
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                if self.dfs(i, 0, color, graph) == False:
                    return False
        return True








# BFS Solution


# from collections import deque
# class Solution(object):
#     def isBipartite(self, graph):
#         color = [-1]*len(graph)
#         for start in range(len(graph)):

#             # Already colored
#             if color[start] != -1:
#                 continue

#             q = deque([start])
#             color[start] = 0
#             while q:
#                 node = q.popleft()
#                 for neighbour in graph[node]:
#                     if color[neighbour] == -1:
#                         color[neighbour] = 1 - color[node]
#                         q.append(neighbour)
#                     elif color[neighbour] == color[node]:
#                         return False
#         return True