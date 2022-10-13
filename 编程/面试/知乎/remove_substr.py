# 给一个字符串 alpha 和另一个字符串 beta 返回字符串 alpha 去除 beta 后的字串，实例说明 alpha:ababccabcaaa; beta:abc 返回 aaa

from os import remove

# 思路：暴力解法，每次删除一个子串，直到不能删除

def remove_substr2(alpha, beta):
    m = len(beta)
    if m == 0:
        return alpha
    while True:
        tmp = ''
        n = len(alpha)
        i = 0
        while i < n:
            k, j = i, 0
            while j < m and k < n and alpha[k] == beta[j]:
                k += 1
                j += 1
            if j < m:
                tmp += alpha[i]
                i += 1
            else:
                i = k
        new_n = len(tmp)
        alpha = tmp
        if n == new_n:
            break
    return alpha

# 思路：每次删除一个子串，然后跳转到子串之前能匹配到的最大为止继续匹配

def remove_substr(alpha, beta):
    m = len(beta)
    if m == 0:
        return alpha
    mark = [0]*len(alpha)
    i, j, k = 0, 0, 0
    while True:
        n = len(alpha)
        while j < m and k < n and alpha[k] == beta[j]:
            mark[k] = max(mark[k], j)
            k += 1
            j += 1
        if j < m:
            i, j, k = i+1, 0, i+1
        else:
            alpha = alpha[0:i]+alpha[k:]
            if i > 0:
                i, j, k = i-mark[i-1]-1, mark[i-1]+1, i
            else:
                i, j, k = 0, 0, 0
        if i == len(alpha):
            break
    return alpha



if __name__ == '__main__':
    print(remove_substr("ababccabcaaa", "abc"))
    print(remove_substr("aaaaaa", "a"))
    print(remove_substr("abcd", "abcd"))