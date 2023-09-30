class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagrams(word1, word2):
            if len(word1) != len(word2): return False
            hm = {}
            for letter in word1:
                hm[letter] = hm.get(letter, 0) + 1
            for letter in word2:
                if not letter in hm:
                    return False
                hm[letter] = hm[letter] - 1
                if hm[letter] < 0:
                    return False
            return True

        ans = []
        for word in words:
            if len(ans) != 0:
                prev = ans[-1]
                if isAnagrams(prev, word):
                    print("checking: " + prev + " and " + word)
                    continue
            ans.append(word)
        return ans

