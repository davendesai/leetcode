class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)

        if n <= k:
            return 1

        freqs = []
        i = 0
        while i < n:
            j = i+1
            while j < n and word[j] == word[i]:
                j += 1
            freqs.append((word[i], j-i))
            i = j

        minimal = [ch for (ch, cnt) in freqs]
        minimal = reduce(lambda ch1, ch2: ch1 + ch2, minimal)
        print("minimal:", minimal)

        extras = [(ch, (cnt-1)) for (ch, cnt) in freqs if cnt > 1]
        print("extras:", extras)

        @cache
        def ways(idx: int, rem: int) -> int:

            # reached the end and had enough extras
            if idx == len(extras) and rem != 0:
                return 0

            # finished extras early
            if rem == 0:
                return 1

            total = 0
            for i in range(extras[idx][1]):
                total += ways(idx+1, rem-i-1)
                
            total += ways(idx+1, rem)
            return total


        mod = ((10**9)+7)
        ans = 0
        """
        for length in range(n, k-1, -1):
            ans += ways(0, length-len(minimal))
        """
        for length in range(len(minimal), k):
            ans += ways(0, length-len(minimal))
            ans %= mod

        possible = 1
        for i in range(len(extras)):
            possible *= extras[i][1]+1
            possible %= mod

        return (possible-ans+mod) % mod

