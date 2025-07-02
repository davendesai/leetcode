from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freqs = Counter(s)
        choices = sorted([ ch for ch, _ in freqs.items() if freqs[ch] >= k])
        print(choices)

        def isSubsequence(ss: str) -> bool:
            if len(ss) > len(s):
                return False
            
            idx = 0
            for ch in s:
                if idx < len(ss) and ch == ss[idx]:
                    idx += 1
            return idx == len(ss)


        queue = deque()
        queue.append("")
        ans = ""

        while queue:
            curr = queue.popleft()
            for ch in choices:
                cand = curr + ch
                if isSubsequence(cand * k):
                    if len(cand) >= len(ans):
                        ans = cand
                    queue.append(cand)

        return ans
