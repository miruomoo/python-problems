class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for c in s:
            if c in hashmap.values():
                stack.append(c)
            elif stack and hashmap[c]==stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False