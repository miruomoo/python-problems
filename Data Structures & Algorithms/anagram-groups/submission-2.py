class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = collections.defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            hashMap[sorteds].append(s)
        return hashMap.values()