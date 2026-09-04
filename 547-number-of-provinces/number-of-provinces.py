class Solution(object):
    def recursion(self, node, visited, adj):
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.recursion(neighbor, visited, adj)
    def findCircleNum(self, isConnected):
        # Converting matrix into list
        n = len(isConnected)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    adj[i].append(j)

        visited = [0]*n
        prov = 0
        for i in range(n):
            if visited[i] == 0:
                prov += 1
                self.recursion(i, visited, adj)
        return prov