# 记录十二生肖，根据年份判断生肖
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# 星座名称
zodiac_name = ('摩羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座',
               '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座')
# 星座日期
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# int_month = int(input('请输入月份：'))
# int_day = int(input('请输入日期：'))
# (month, day) = (5, 26)
#
# zodiac_day = filter(lambda x: x <= (month, day), zodiac_days)
# zodiac_len = len(list(zodiac_day)) % 12
#
# print(zodiac_name[zodiac_len])

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

z_num = {}
for i in zodiac_name:
    z_num[i] = 0

while True:
    # 用户输入出生年月日
    year = int(input('请输入年份：'))
    month = int(input('请输入月份：'))
    day = int(input('请输入日期：'))

    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 23:
            break
        n += 1
    # 输出生肖和星座
    print(zodiac_name[n])
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))

    # 记录输出的生肖和星座
    cz_num[chinese_zodiac[year % 12]] += 1
    z_num[zodiac_name[n]] += 1

    # 输出记录的生肖和星座的统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))
    for each_key in z_num.keys():
        print(('星座 %s 有 %d 个') % (each_key, z_num[each_key]))
