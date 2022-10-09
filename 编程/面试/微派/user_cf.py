import math

# 给定一个用户评分矩阵，找出每个用户最相似用户

def cosine(u, v):
    n = len(u)
    son = 0
    mom_u = 0    
    mom_v = 0
    for i in range(n):
        son += u[i]*v[i]
        mom_u += u[i]**2
        mom_v += v[i]**2
    return son/math.sqrt(mom_u)/math.sqrt(mom_v) if mom_u != 0 and mom_v != 0 else -1 # 注意边界

def lookalike(rate_matrix):
    n, m = len(rate_matrix), len(rate_matrix[0])
    avg_rate = [0]*m
    for i in range(m): # 消除用户打分偏置
        for j in range(n):
            avg_rate[i] += rate_matrix[j][i]
        avg_rate[i] = avg_rate[i]/n
    
    for i in range(m):
        for j in range(n):
            rate_matrix[j][i] = rate_matrix[j][i]-avg_rate[i]

    # sim compute
    most_like_user = [-1]*n
    for i in range(n):
        max_sim = -1
        for j in range(n):
            score = cosine(rate_matrix[i], rate_matrix[j])
            if i != j and score > max_sim:
                most_like_user[i] = j
                max_sim = score
    return most_like_user

if __name__ == '__main__':
    matrix = [[5,0,3,1,0],[0,3,0,3,0],[0,2,4,4,1],[4,4,5,0,0],[2,4,0,5,2]]
    user_like = lookalike(matrix)
    print(user_like)


