class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        tcount = collections.defaultdict(int)
        scount = collections.defaultdict(int)
        res = ""
        resLen = float("inf")
        for c in t:
            tcount[c]+=1
        need = len(tcount)
        have = 0
        l = 0
        for r in range(len(s)):
            scount[s[r]]+=1
            if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                have+=1
            while have==need:
                if (r-l+1)<resLen:
                    res = s[l:r+1]
                    resLen = (r-l+1)
                scount[s[l]] -=1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        return res
