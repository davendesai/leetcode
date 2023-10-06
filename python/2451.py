class Solution:
    def oddString(self, words: List[str]) -> str:
        diffs = []
        for word in words:
            d = []
            for i in range(len(word) - 1):
                d.append(ord(word[i+1]) - ord(word[i]))
            diffs.append(d)

        for i in range(len(diffs)):
            if diffs.count(diffs[i]) == 1:
                return words[i]
        

