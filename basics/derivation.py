# 从 1 到 10 所有偶数的平方
a_list = []
for i in range(1, 11):
    if i % 2 == 0:
        a_list.append(i * i)
print(a_list)

# 列表推导式
b_list = [i * i for i in range(1, 11) if (i % 2 == 0)]
print(b_list)

#
z_num = {}
for i in a_list:
    z_num[i] = 0

# 字典推导式
b_num = {i: 0 for i in a_list}
