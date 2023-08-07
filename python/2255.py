class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ret = 0
        for word in words:
            if len(word) > len(s):
                continue

            if word == s[:len(word)]:
                ret += 1
        return ret

