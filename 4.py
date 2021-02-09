class Solution:
    def interpret(self, command: str) -> str:
        s = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                s += 'G'
                i += 1
            else:
                if i < len(command) and command[i + 1] == ')':
                    s += 'o'
                    i += 2
                else:
                    i += 4
                    s += 'al'
        return s