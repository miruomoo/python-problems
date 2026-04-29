class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        graph = collections.defaultdict(list)

        for node, neighbor in edges:
            graph[node].append(neighbor)
            graph[neighbor].append(node)
        
        visited = set()

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n


        