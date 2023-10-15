class Solution:
    def finalString(self, s: str) -> str:
        ans = []
        i = 0
        while i < len(s):
            if s[i] != 'i':
                ans.append(s[i])
                i += 1
                continue

            j = i
            while j < len(s) and s[j] == 'i':
                j += 1
            if j - i % 2 != 0:
                tmp = []
                while ans:
                    tmp.append(ans.pop())
                ans = tmp

            i += 1

        return "".join(ans)
        
