class Solution(object):
    def dfs(self, node, adj, visited):
        visited[node] = 1
        for neighbor in adj[node]:
            if visited[neighbor] == 0:
                self.dfs(neighbor, adj, visited)
    def findCircleNum(self, isConnected):
        

        # BFS

        # visited = set()
        # n = len(isConnected)
        # prov = 0

        # def bfs(val):
        #     queue = deque()
        #     queue.append(val)
        #     while queue:
        #         curr = queue.popleft()
        #         if curr in visited:
        #             continue
        #         visited.add(curr)

        #         for i in range(n):
        #             if isConnected[curr][i] ==1 and i not in visited:
        #                 queue.append(i)
        # for j in range(n):
        #     if j not in visited:
        #         bfs(j)
        #         prov +=1
        # return prov


        
        
        # DFS using adj matrix
        
        # visited = set()
        # n = len(isConnected)
        # prov = 0

        # def dfs(val):
        #     visited.add(val)

        #     for i in range(n):
        #         if isConnected[val][i] == 1 and i not in visited:
        #             dfs(i)

        # for i in range(n):
        #     if i not in visited:
        #         dfs(i)
        #         prov +=1
        # return prov



    # DFS using adj listt

        n = len(isConnected)
        adj = [[]for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        visited = [0]*n
        provinces = 0

        for i in range(n):
            if visited[i] == 0:
                provinces +=1
                self.dfs(i, adj, visited)
        return provinces


        
