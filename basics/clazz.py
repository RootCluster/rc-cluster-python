# 对象
def print_role(role_name):
    print('name is %s ,hp is %s' % (role_name['name'], role_name['hp']))


# 定义了一个玩家类
class Player():
    # __init__ 类实例化之后自动执行
    def __init__(self, name, hp, occu):
        # 类中的属性不想在外部直接被访问时，需要在属性前加入'__'，例如 self.__name
        # self.__name = name
        self.name = name
        self.hp = hp
        self.occu = occu

    # 定义一个方法
    def print_role(self):
        print('%s: %s %s' % (self.name, self.hp, self.occu))

    # 定义一个修改名字的方法
    def update_name(self, new_name):
        self.name = new_name


class Monster():
    '定义怪物类'

    # 暂时不想写具体内容时，可以用 pass
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物的父类')


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        # 父类中初始化了 hp，子类中不需要重复初始化
        super().__init__(hp)


class Boss(Monster):
    'Boss 怪物'

    # 覆盖父类的 whoami 方法
    def whoami(self):
        print('我是怪物，我怕谁')


# 类的实例化
user1 = Player('tom', 100, 'war')
user2 = Player('jerry', 90, 'master')
user1.print_role()
user2.print_role()

user1.update_name('wilson')
user1.print_role()

a1 = Monster(1000)
print(a1.hp)
print(a1.run())

a2 = Animals(1)
print(a2.hp)
print(a2.run())

a3 = Boss(5000)
print(a3.whoami())
