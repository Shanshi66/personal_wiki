from unicodedata import digit


class Solution:
    def reformatNumber(self, number: str) -> str:
        digit = []
        tmp = ''
        for num in number:
            if not '0' <= num <= '9':
                continue
            tmp += num
            if len(tmp) == 3:
                digit.append(tmp)
                tmp = ''
        if tmp:
            digit.append(tmp)

        if len(digit) >= 2 and len(digit[-1]) == 1:
            new_digit = '{}{}-{}{}'.format(digit[-2][0], digit[-2][1],digit[-2][2], digit[-1])
            digit.pop()
            digit.pop()
            digit.append(new_digit)
        return '-'.join(digit)



if __name__ == '__main__':
    test = Solution()
    print(test.reformatNumber("1-23-45 6"))
    print(test.reformatNumber("123 4-567"))
    print(test.reformatNumber("123 4-5678"))
    print(test.reformatNumber("12"))
    print(test.reformatNumber("--17-5 229 35-39475 "))
    print(test.reformatNumber("--17"))

        