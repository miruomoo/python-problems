class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        freq.reverse()
        res = []
        for i in range(len(freq)):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
