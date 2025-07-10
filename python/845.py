class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)

        if n < 3: return 0

        mountains = []
        ans = 0

        i = 1
        while i < n-1:
            l, r = i-1, i+1

            # found summit
            if arr[l] < arr[i] and arr[r] < arr[i]:

                # gradually expand borders
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1

                while r < n-1 and arr[r] > arr[r+1]:
                    r += 1

                mountains.append(arr[l:r+1])
                ans = max(ans, r-l+1)
                i = r

            else:
                i += 1

        print(mountains)
        return ans    

