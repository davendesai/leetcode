class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1, w2 = defaultdict(int), defaultdict(int)

        for w in s1.split():
            w1[w] += 1
        for w in s2.split():
            w2[w] += 1

        uncommon = []

        for w in w1:
            if w1[w] == 1 and w2[w] == 0:
                uncommon.append(w)

        for w in w2:
            if w2[w] == 1 and w1[w] == 0:
                uncommon.append(w)

        return uncommon
