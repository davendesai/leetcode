"""
class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            add = ""
            for ch in word:
                if ch == 'z':
                    add += 'a'
                else:
                    add += chr(ord(ch)+1)
            word += add

        return word[k-1]
"""        

class Solution:
    def kthCharacter(self, k: int) -> str:
        offset = 0
        
        while k > 1:
            # max pwr of 2 < than k            
            n = k.bit_length()-1

            # if k is pwr of 2 then don't over subtract
            if (1<<n) == k:
                n -= 1

            k -= 1<<n
            offset += 1

        return chr(ord('a') + offset)
