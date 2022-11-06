class Solution:
    def interpret(self, command: str) -> str:
        n = len(command)
        i = 0
        res = ''
        while i < n:
            if command[i] == 'G':
                res += 'G'
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                res += 'o'
                i += 2
            elif command[i] == '(' and command[i+1] == 'a':
                res += 'al'
                i += 4
        return res

if __name__ == '__main__':
    test = Solution()
    print(test.interpret("G()(al)"))
    print(test.interpret("G()()()()(al)"))
    print(test.interpret("(al)G(al)()()G"))