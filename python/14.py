class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for idx in range(1, len(strs)):
            s = strs[idx]
            while prefix != s[:len(prefix)]:
                prefix = prefix[:-1]
        return prefix
        

