class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [float("inf")] * n
        graph[src] = 0

        for i in range(k + 1):
            tempGraph = graph.copy()

            for s, d, p in flights:
                if graph[s] == float("inf"):
                    continue
                if graph[s] + p < tempGraph[d]:
                    tempGraph[d] = graph[s] + p

            graph = tempGraph

        return graph[dst] if graph[dst] != float("inf") else -1