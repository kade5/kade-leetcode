class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph, p_count = self.buildGraph(numCourses, prerequisites)
        stack = []
        course_order = []

        for c in range(numCourses):
            if p_count[c] == 0:
                stack.append(c)

        while stack:
            course = stack.pop()
            course_order.append(course)

            for c in graph[course]:
                p_count[c] -= 1
                if p_count[c] == 0:
                    stack.append(c)

        if len(course_order) != numCourses:
            return []

        return course_order

    def buildGraph(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        p_count = [0] * numCourses

        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            p_count[pair[0]] += 1

        return graph, p_count
