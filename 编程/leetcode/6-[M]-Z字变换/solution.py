# 先对字符串进行补足，然后从上往下层次遍历

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        add_len = 2*(numRows-1)-len(s)%(2*(numRows-1))+1 # 以2*(n-1)个字符为一组
        new_s = s + '#'*add_len
        queue = []
        index_set = set()
        result = []
        i = 0
        while i < len(new_s):
            queue.append(i)
            index_set.add(i)
            i += 2*(numRows-1)
        i = 0
        while i < len(queue):
            front = queue[i]
            i += 1
            if new_s[front] != '#':
                result.append(new_s[front])
            if front-1 not in index_set and front-1 > 0:
                queue.append(front-1)
                index_set.add(front-1)
            if front+1 not in index_set and front+1 < len(s):
                queue.append(front+1)
                index_set.add(front+1)
        new_str = ''.join(result)
        return new_str


if __name__ == '__main__':
    test = Solution()
    print(test.convert("PAYPALISHIRING", 3))
    print(test.convert("PAYPALISHIRING", 4))
    print(test.convert("PAYPALISHIRING", 100))
    print(test.convert("ABCD", 3))
    print(test.convert("ABCDE", 4))
    print(test.convert("ABCDE", 3))
    print(test.convert("A", 1))

        
        