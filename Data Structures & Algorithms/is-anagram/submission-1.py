class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = collections.defaultdict(int)
        for x in s:
            hashMap[x] += 1
        for x in t:
            hashMap[x] -= 1
            if hashMap[x] < 0:
                return False
        return True