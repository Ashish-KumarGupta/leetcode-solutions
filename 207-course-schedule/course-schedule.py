from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj[u].append(v)
            
        indegree = [0] * numCourses
        for i in range(numCourses):
            for neighbour in adj[i]:
                indegree[neighbour] += 1
                
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                
        topo = []
        while q:
            node = q[0]
            q.popleft()
            topo.append(node)
            
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        if(len(topo) == numCourses):
            return True
        return False