# 求时钟上时针和分针夹角为6度的时间刻度，只需求分针为整数刻度即可

def transform(minutes):
    hour = minutes // 60
    minute = minutes % 60
    return '{}:{}'.format(hour, minute)


# 思路1：遍历每一分钟，看是否满足条件
# 时间复杂度：24*60

def six_time():
    time_list = []
    for i in range(24*60+1):
        angle = 6*i - 0.5*i
        if angle % 360 == 6 or angle%360 == 354:
            time = transform(i)
            time_list.append(time)
    return time_list

# 思路2：枚举可能得夹角，看是否是5.5的倍数（每分钟分针比时针多走5.5度）
# 时间复杂度：循环12次，分针最多转12圈

def six_time2():
    time_list = []
    for i in range(12):
        total_angle = 6+360*i
        if (total_angle*10) % 55 == 0:
            time = total_angle/5.5
            time_list.append(transform(int(time)))
        total_angle = 354+360*i
        if (total_angle*10) % 55 == 0:
            time = total_angle/5.5
            time_list.append(transform(int(time)))
    return time_list

# 思路3：分针一定在整数刻度上，分针每次走6度，那么时针一定也在分针的刻度上。只有12,24,36,48,60这几个分钟时刻，时针可能重合，因此只需要枚举这些分钟时刻左右两边时针位置是否可行即可。
# 时间复杂度：循环10次

if __name__ == '__main__':
    # print(six_time())
    print(six_time2())