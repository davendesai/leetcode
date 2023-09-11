class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        words = text.split(' ')

        i = -1
        while first in words[i+1:len(words)-2]:
            i = words.index(first, i+1, len(words)-2)
            if words[i+1] == second:
                res.append(words[i+2])
        
        return res

