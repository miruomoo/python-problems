class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.defaultdict(int)
        buckets = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]+=1
        for key, value in count.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
