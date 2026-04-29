class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hashMap = collections.defaultdict(int)
        for c in s:
            hashMap[c]+=1
        for c in t:
            hashMap[c]-=1
            if hashMap[c]<0:
                return False
        return True

