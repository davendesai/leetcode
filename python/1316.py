class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        substrs = set()

        for i in range(len(text)-1):
            for j in range(i+1, len(text)):
                length = j-i
                remaining = len(text)-j

                if remaining < length:
                    break

                first = text[i:j]
                last = text[j:j+length]

                if first == last:
                    substrs.add(text[i:i+length]*2)

        print(substrs)
        return len(substrs)
