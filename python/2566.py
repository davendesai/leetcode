class Solution:
    def minMaxDifference(self, num: int) -> int:
        idx9, idx0 = 0, 0
        strNum = str(num)

        for i in range(len(strNum)):
            d = strNum[i]
            if d != '9':
                idx9 = i
                break

        for i in range(len(strNum)):
            d = strNum[i]
            if d != '0':
                idx0 = i
                break

        maxStr = strNum.replace(strNum[idx9], "9")
        minStr = strNum.replace(strNum[idx0], "0")

        return int(maxStr) - int(minStr)        
       


