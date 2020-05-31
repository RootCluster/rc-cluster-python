# 异常有多种
# i = j (not defined 未定义错误);

# 编写程序的语法错误 (syntaxError);

# a ='123'
# print(a[3])
# 这里会出现数组越界（indexError）;

# b = {'a':1, 'b':2}
# print(b['c'])
# 这里出现键错误（keyError）;

# 当用户输入非数字时进行提示
try:
    year = int(input('input year：'))
except ValueError as e:
    print('年份请输入数字 %s' % e)

# 文件操作
try:
    file_write = open('name.txt', 'w')
except Exception as e:
    print(e)
finally:
    file_write.close()
