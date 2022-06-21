class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X' , 'IX', 'V', 'IV', 'I']
        digit = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = []
        while num > 0:
            for i in range(len(roman)):
                if num >= digit[i]:
                    result.append(roman[i])
                    num -= digit[i]
                    break
        return ''.join(result)

if __name__ == '__main__':
    test = Solution()
    print(test.intToRoman(3))
    print(test.intToRoman(1))
    print(test.intToRoman(4))
    print(test.intToRoman(9))
    print(test.intToRoman(58))
    print(test.intToRoman(1994))
    print(test.intToRoman(10))
    print(test.intToRoman(1000))
    print(test.intToRoman(899))
