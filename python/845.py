class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)

        if n < 3: return 0

        mountains = []

        def climb(i):
            while i < n-1 and arr[i] < arr[i+1]:
                i += 1
            return i

        def descend(i):
            while i < n-1 and arr[i] > arr[i+1]:
                i += 1
            return i
            
        ans = 0

        # mountains have to start at a low
        # i.e. be increasing
        j = 0

        while j < n:
            # advance till base
            while j < n-1 and arr[j] >= arr[j+1]:
                j += 1

            summit = climb(j)
            if summit == n-1:
                break
            bottom = descend(summit)

            if summit-j+1 > 1 and bottom-summit+1 > 1:
                mountain = arr[j:bottom+1]
                ans = max(ans, len(mountain))
                mountains.append(mountain)

            j = bottom

        print(mountains)
        return ans

