class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 0
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                ans += 1
        return ans+1
            
