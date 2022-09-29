
# 题中字符串左移了K位，枚举K

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        for i in range(1, len(s1)):
            for j in range(len(s1)):
                if s1[j] != s2[j-i]:
                    break
            else:
                return True
        return False


# 如果s2由s1旋转得到，那么s2一定在s1+s1中

class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1+s1


if __name__ == '__main__':
    test = Solution()
    print(test.isFlipedString("waterbottle", "erbottlewat"))
    print(test.isFlipedString("waterbottle", "erbottlewac"))
