class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        start = 0
        ans = 0
        for idx, c in enumerate(s):
            if c in chars:
                # start new seq from last occurence
                start = max(start, chars[c] + 1)

            # unique char just continue and note the idx
            chars[c] = idx

            curr = idx - start + 1
            ans = max(ans, curr)
        return ans