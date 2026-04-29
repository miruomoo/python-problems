class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}
        for i, c in enumerate(s):
            hmap[c] = i

        res = []
        start = 0
        maxIndex = 0
        for i, c in enumerate(s):
            maxIndex = max(hmap[c], maxIndex)
            if i == maxIndex:
                res.append(maxIndex - start + 1)
                start = i + 1

        return res



