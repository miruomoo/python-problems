class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()

        adj = collections.defaultdict(list)
        for src, des in tickets:
            adj[src].append(des)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False

            temp = list(adj[src])
            for i, n in enumerate(temp):
                res.append(n)
                adj[src].remove(n)
                if dfs(n):
                    return True
                adj[src].insert(i, n)
                res.pop()

            return False

        dfs("JFK")
        return res