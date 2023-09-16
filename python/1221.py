class Solution:
    def balancedStringSplit(self, s: str) -> int:
        total, cnt = 0, 0
        for c in s:
            if c == 'R':
                cnt += 1
            if c == 'L':
                cnt -= 1
            if cnt == 0:
                total +=1
        return total

