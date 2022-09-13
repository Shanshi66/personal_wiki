class Solution:
    def maximumSwap(self, num: int) -> int:
        digit = []
        max_digit = []
        while num:
            d = num%10
            digit.append(d)
            if max_digit and d <= max_digit[-1][0]:
                max_digit.append(max_digit[-1])
            else:
                max_digit.append((d, len(digit)-1))
            num = num//10
        for i in range(len(digit)-1, -1, -1):
            if digit[i] < max_digit[i][0]:
                digit[i], digit[max_digit[i][1]] = digit[max_digit[i][1]], digit[i]
                break
        result = 0
        for d in digit[::-1]:
            result = result*10+d
        return result


if __name__ == '__main__':
    test = Solution()
    print(test.maximumSwap(2736))
    print(test.maximumSwap(9973))
    print(test.maximumSwap(9937))
    print(test.maximumSwap(9037))
    print(test.maximumSwap(0))
    print(test.maximumSwap(1993))
