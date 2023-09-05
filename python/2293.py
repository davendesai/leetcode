class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        def algo(arr):
            for i in range(len(arr) // 2):
                j, k = i * 2, i * 2 + 1
                if i % 2 == 0:
                    arr[i] = min(arr[j], arr[k])
                else:
                    arr[i] = max(arr[j], arr[k])
            
            return arr[:len(arr) // 2]

        while len(nums) != 1:
            nums = algo(nums)

        return nums[0]
