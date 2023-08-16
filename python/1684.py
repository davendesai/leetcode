class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check = set(allowed)

        inv_count = 0
        for w in words:
            for c in w:
                if c not in check:
                    inv_count += 1
                    break
        return len(words) - inv_count
            


