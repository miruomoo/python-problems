class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = collections.defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]

        for num in nums:
            hashMap[num]+=1
        for key, value in hashMap.items():
            buckets[value].append(key)
        res = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res

