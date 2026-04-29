class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in hashMap.values():
                stack.append(c)
            elif stack and hashMap[c]==stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False