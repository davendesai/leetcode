class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []

        for word in words:
            inner_words = word.split(separator)
            for i_w in inner_words:
                if len(i_w) > 0:
                    res.append(i_w)

        return res

