class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        res = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return res