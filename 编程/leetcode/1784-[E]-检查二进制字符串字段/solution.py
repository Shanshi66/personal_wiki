class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        one_num = 0
        one_flag = False
        for c in s:
            if c == '1':
                one_flag = True
            else:
                if one_flag:
                    one_num += 1
                one_flag = False
        if one_flag:
            one_num += 1

        return True if one_num < 2 else False



if __name__ == '__main__':
    test = Solution()
    print(test.checkOnesSegment("1001"))
    print(test.checkOnesSegment("110"))
    print(test.checkOnesSegment("111"))