# 打开文件函数
def func_file(file_name):
    print(open(file_name).read())


func_file('name.txt')


# 多参数函数
def func_multi(a, b, c):
    print('a = %s' % a)
    print('b = %s' % b)
    print('c = %s' % c)


func_multi(1, 2, 3)
# 调用函数可以指定参数，这样可与函数定义参数位置无关
func_multi(100, c=300, b=200)


# 可变参数函数，用*表示
def func_variable(x, *y):
    print(x + len(y))


# 函数迭代器
list1 = [1, 2, 3]
item = iter(list1)
# 输出第一个元素
print(next(item))
# 输出第二个元素
print(next(item))

# 取出 [20,30) 的数据，步长为 2
for i in range(20, 30, 2):
    print(i)


# 取出 [20,30) 的数据，步长为 0.5
def cusom_range(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in cusom_range(20, 30, 0.5):
    print(i)

# ================= 闭包 =================#
# def func():
#     a = 1
#     b = 2
#     return a + b
#
#
# def sum(a):
#     def add(b):
#         return a + b
#
#     # add 函数名称或函数的引用
#     # add() 函数的调用
#     return add
#
#
# num1 = func()
# num2 = sum(2)


# 计数器闭包函数
# def counter(First=0):
#     cnt = [First]
#
#     def add_one():
#         cnt[0] += 1
#         return cnt[0]
#
#     return add_one
#
#
# num3 = counter(5)
# print(num3)

# 装饰器
import time


def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print('运行时间是 %s 秒' % (stop_time - start_time))

    return wrapper


@timmer
def i_can_sleep():
    time.sleep(3)


# 调用函数
i_can_sleep()


# 带参数的装饰器
def new_tips(args):
    def tips(func):
        def nei(a, b):
            print('start %s' % args)
            # 取得函数的名称 func.__name__
            print('start %s and func name %s' % (args, func.__name__))
            func(a, b)
            print('stop')

        return nei

    return tips


@new_tips('add_model')
def add(a, b):
    print(a + b)


@new_tips('sub_model')
def sub(a, b):
    print(a - b)


# 函数调用
print(add(1 + 2))
print(sub(3 - 1))
