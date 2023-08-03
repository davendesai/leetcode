class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
            
        lim = len(arr) // 4

        prev = arr[0]
        count = 1
        for n in arr[1:]:
            if n == prev:
                count += 1
                if count > lim:
                    return n
            else:
                prev = n
                count = 1

