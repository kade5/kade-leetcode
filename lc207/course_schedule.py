class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        visited = set()
        graph = self.buildGraph(numCourses, prerequisites)
        path = set()
        completable = True

        def dfs(course):
            nonlocal completable
            if not completable:
                return

            if course not in visited:
                visited.add(course)

            for c in graph[course]:
                if c in path:
                    completable = False
                    return
                path.add(c)
                dfs(c)
                path.remove(c)

        for course in range(numCourses):
            if course not in visited:
                dfs(course)

        return completable

    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        return graph
