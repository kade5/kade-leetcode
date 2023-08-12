class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = self.buildGraph(numCourses, prerequisites)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            
            visited.add(course)

            for prereq in graph[course]:
                if not dfs(prereq): return False
            
            visited.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True


    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])

        return graph
