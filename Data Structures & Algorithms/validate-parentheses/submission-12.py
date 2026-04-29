class Solution:
    def isValid(self, s: str) -> bool:

        hmap = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        stack = []

        for c in s:

            if c in hmap.values():
                stack.append(c)

            elif stack and stack[-1] == hmap[c]:
                stack.pop()

            else:
                return False

        return True if not stack else False
