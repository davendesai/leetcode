class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        hm = {}
        for word in words:
            for ch in word:
                hm[ch] = hm.get(ch, 0) + 1
        for val in hm.values():
            if val % n != 0:
                return False
        return True

