class Solution(object):
    def dfs(self, node, graph, visited, pathvisited, order):
        visited[node] = 1
        pathvisited[node] = 1
        for neighbour in graph[node]:
            # when the node is not visited
            if visited[neighbour] == 0:
                if self.dfs(neighbour, graph, visited, pathvisited, order) == True:
                    return True
            # if the node has been previously visited
            # but it has to be visited on the same path
            elif(pathvisited[neighbour]):
                return True
        
        pathvisited[node] = 0
        order.append(node)
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        visited = [0]*numCourses
        pathvisited = [0]*numCourses
        order = []
        
        for i in range(numCourses):
            if visited[i] == 0:
                if self.dfs(i, graph, visited, pathvisited, order) == True:
                    return []

        order.reverse()

        return order
        
        