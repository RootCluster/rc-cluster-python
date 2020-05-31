# 将小说的主要人物记录在文件中
# 整个流程 open() --> write() --> close()
# 'w' 标识是可以写入数据，会覆盖原内容
# 'a' 标识是在原数据后面添加新内容
file_write = open('name.txt', 'w')
file_write.write('诸葛亮')
file_write.close()

# 读取文件
# 整个流程 open() --> read() --> close()
file_read = open('name.txt')
print(file_read.read())
file_read.close()

# 读取一行
file_line = open('name.txt')
print(file_line.readline())

# 读取每一行
file_each_line = open('name.txt')
for line in file_each_line.readlines():
    print(line)
    print("============")

# 操作完文件，回到开头
file_seek = open('name.txt')
# 查看文件的指针位置
print('当前文件的指针位置' % file_seek.tell())
# 读取一个字符
file_seek.read(1)
# 查看文件的指针位置
print('当前文件的指针位置' % file_seek.tell())
# seek()函数，
# 第一个参数代表偏移位置；
# 第二个参数 0 表示从文件开头偏移，1 表示从当前位置偏移，2 表示从文件结尾位置偏移
file_seek.seek(0)
# 查看文件的指针位置
print('当前文件的指针位置' % file_seek.tell())
file_seek.close()

# ================== 常用的一些文件操作示例 ==================#

# 获取文件中形如：A|B|C|D|E 形式的文件内容
file_a = open('name1.txt')
data_a = file_a.read()
print(data_a.split('|'))

# 获取文件中存放在奇数行的文件内容
file_b = open('name2.txt')
data_b = file_b.read()
i = 1
for line in file_b.readlines():
    if i % 2 == 1:
        # 去除换行符
        print(line.strip('\n'))
    i += 1
