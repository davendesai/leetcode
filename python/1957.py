class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []
        for c in s:
            if len(stack) > 1 and stack[-1] == c and stack[-2] == c:
                stack.pop()
            stack.append(c)
        return ''.join(stack)

