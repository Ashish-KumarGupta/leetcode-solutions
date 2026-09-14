from collections import deque
class Solution(object):
    def isBipartite(self, graph):
        color = [-1]*len(graph)
        for start in range(len(graph)):

            # Already colored
            if color[start] != -1:
                continue

            q = deque([start])
            color[start] = 0
            while q:
                node = q.popleft()
                for neighbour in graph[node]:
                    if color[neighbour] == -1:
                        color[neighbour] = 1 - color[node]
                        q.append(neighbour)
                    elif color[neighbour] == color[node]:
                        return False
        return True