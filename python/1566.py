class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        endP = len(arr) - (m * k)

        for i in range(endP + 1):
            patt = arr[i:i + m]
            poss = arr[i:i + m * k]
            if patt * k == poss:
                return True

        return False

