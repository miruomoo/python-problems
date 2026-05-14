class CountSquares:

    def __init__(self):
        self.counter = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0

        px, py = point
        for x, y in self.points:
            if px == x or py == y or abs(px - x) != abs(py - y):
                continue
            res += self.counter[(px, y)] * self.counter[(x, py)]

        return res
        
