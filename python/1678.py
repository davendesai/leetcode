class Solution:
    def interpret(self, command: str) -> str:
        res = ""

        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'

            if command[i] == '(':
                j = i
                while command[j] != ')': j += 1
                if j - i > 1:
                    res += "al"
                else:
                    res += "o"
        return res

