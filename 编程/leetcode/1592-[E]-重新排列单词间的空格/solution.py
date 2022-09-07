class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.strip().split()
        space_num = len(text) - len(''.join(words))
        if len(words) == 1:
            return words[0]+" "*space_num
        space_left = space_num % (len(words)-1)
        space_seg = space_num//(len(words)-1)
        space_seg_str = ' '*space_seg
        return space_seg_str.join(words)+' '*space_left



if __name__ == '__main__':
    test = Solution()
    print(test.reorderSpaces("  this   is  a sentence "))
    print(test.reorderSpaces(" practice   makes   perfect"))
    print(test.reorderSpaces("hello   world"))
    print(test.reorderSpaces("  walks  udp package   into  bar a"))
    print(test.reorderSpaces("a"))