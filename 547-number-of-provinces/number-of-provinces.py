class Solution(object):
    def findCircleNum(self, isConnected):
        
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

        visited = set()
        n = len(isConnected)
        prov = 0

        def dfs(val):
            visited.add(val)

            for i in range(n):
                if isConnected[val][i] == 1 and i not in visited:
                    dfs(i)

        for i in range(n):
            if i not in visited:
                dfs(i)
                prov +=1
        return prov