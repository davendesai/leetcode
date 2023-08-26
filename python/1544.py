class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack:
                curr, prev = s[i], stack[-1]
                if (prev.islower() and curr == prev.upper()) or (prev.isupper() and curr == prev.lower()):
                    stack.pop()
                    continue
            stack.append(s[i])
        return "".join(stack) 

