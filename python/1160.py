class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hm = {}
        for c in chars:
            hm[c] = hm.get(c, 0) + 1

        ans = 0
        for w in words:
            wm = {}
            for c in w:
                wm[c] = wm.get(c, 0) + 1

            fits = True
            for c in wm.keys():
                if not c in hm or wm[c] > hm[c]:
                    fits = False
                    break

            if fits:
                ans += len(w)

        return ans


