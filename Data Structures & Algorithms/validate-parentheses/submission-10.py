class Solution:
    def isValid(self, s: str) -> bool:
        cmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []
        for c in s:
            if c in cmap.values():
                stack.append(c)
            elif stack and cmap[c]==stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False