# python 中标准库应用比较广泛的是
# 1. 文章处理的 re
# 2. 日期类型的 time，datetime
# 3. 数字和数学类型的 math，random
# 4. 文件和目录访问的 pathlib，os.path
# 5. 数据压缩和归档的 tarfile
# 6. 通用操作系统的 os，logging，argparse
# 7. 多线程的 threading，queue
# 8. Internet 数据护理的 base64，json，urllib
# 9. 结构化标记处理工具的 HTML，XML
# 10. 开发工具 unitest
# 11. 调试工具 timeit
# 12. 软件包发布的 venv
# 13. 运行服务的 __main__

import re

p = re.compile('a')
print(p.match('a'))

# 正则表达式相关教程 https://github.com/ziishaned/learn-regex/blob/master/translations/README-cn.md
# . ：句号匹配任意单个字符除了换行符
# [ ] ：字符种类。匹配方括号内的任意字符
# [^ ] ：否定的字符种类。匹配除了方括号里的任意字符
# * ：匹配>=0个重复的在*号之前的字符
# + ：匹配>=1个重复的+号前的字符
# ? ：标记?之前的字符为可选
# {n,m} ：匹配num个大括号之前的字符或字符集 (n <= num <= m)
# (xyz) ：字符集，匹配与 xyz 完全相等的字符串.
# | ：或运算符，匹配符号前或后的字符
# \ ：转义字符,用于匹配一些保留的字符 [ ] ( ) { } . * + ? ^ $ \ |
# ^ ：从开始行开始匹配
# $ ：从末端开始匹配
# ^$ ：表示空行
# .*? ：贪婪模式
