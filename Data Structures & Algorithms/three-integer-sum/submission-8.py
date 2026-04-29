class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p, n, z = [],[],[]
        res = set()
        for num in nums:
            if num>0:
                p.append(num)
            elif num<0:
                n.append(num)
            else:
                z.append(num)
        P = set(p)
        N = set(n)
        if len(z)>2:
            res.add((0,0,0))
        if z:
            for num in P:
                if num*-1 in N:
                    res.add((0, num, num*-1))
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                comp = p[i]+p[j]
                if comp*-1 in N:
                    res.add(tuple(sorted([p[i], p[j], comp*-1])))
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                comp = n[i]+n[j]
                if comp*-1 in P:
                    res.add(tuple(sorted([n[i], n[j], comp*-1])))
        return [list(item) for item in res]