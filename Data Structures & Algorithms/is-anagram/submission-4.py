class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
        scount = Counter(s)

        for c in t:
            scount[c] -= 1
            if scount[c] < 0:
                return False

        return True