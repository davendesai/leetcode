class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        res = []

        for w in words:
            if len(w) < 3:
                res.append(w.lower())
            else:
                res.append(w[0].upper() + w[1:].lower())
        return " ".join(res)

