# 记录十二生肖，根据年份判断生肖
chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'

# 从前往后，输出下标从 [0, 3) 区间的数据
# print(chinese_zodiac[0:4])

# 从后往前，输出第一个元素
# print(chinese_zodiac[-1])

year = 2020
# 计算出当前输入年是什么生肖
print(chinese_zodiac[year % 12])
