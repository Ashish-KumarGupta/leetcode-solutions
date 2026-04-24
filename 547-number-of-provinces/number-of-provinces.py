class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = set()
        n = len(isConnected)
        prov = 0

        def bfs(val):
            queue = deque()
            queue.append(val)
            while queue:
                curr = queue.popleft()
                if curr in visited:
                    continue
                visited.add(curr)

                for i in range(n):
                    if isConnected[curr][i] ==1 and n not in visited:
                        queue.append(i)
        for j in range(n):
            if j not in visited:
                bfs(j)
                prov +=1
        return prov