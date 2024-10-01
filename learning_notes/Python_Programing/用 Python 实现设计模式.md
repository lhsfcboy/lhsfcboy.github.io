已剪辑自: https://zhuanlan.zhihu.com/p/31700225

Patterns mean "I have run out of language." - Rich Hickey
之前学习设计模式的时候总是没有什么感觉，因为记性不好一直没记住多少。python不像java中比较强调设计模式(编程套路)，动态语言也内置了像是装饰器、迭代器等模式，另外python中的『一切皆对象』、鸭子类型等也导致python中实现的设计模式和其他语言有些差别。根据YAGNI(you aren't gonna need it)和KISS(Keep it simple sutpid)原则，如果能用简单易懂的方式实现，最好不要滥用设计模式以免增加复杂度和维护难度。本博客是《Mastering Python Design Patterns》的读书笔记，涵盖大部分设计模式(力求pythonic实现)，有兴趣可以参考下，代码示例版本为python3.5.2。
1: The Fctory Pattern(工厂模式: 解决对象创建问题)
先来看三种创建模式中的第一种工厂模式。 解释：处理对象创建，客户端可以申请一个对象而不用知道对象被哪个class创建。可以方便地解耦对象的使用和创建。有两种实现，工厂方法和抽象工厂.
Factory Method(工厂方法)：执行单独的函数，通过传参提供需要的对象的信息。通过一个demo看看例子:
import json
import xml.etree.ElementTree as etree

class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """ 工厂方法 """
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)
Abstract Factory(抽象工厂: 解决复杂对象创建问题)
工厂方法适合对象种类较少的情况，如果有多种不同类型对象需要创建，使用抽象工厂模式。以实现一个游戏的例子说明，在一个抽象工厂类里实现多个关联对象的创建：
class Frog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """ 不同类型玩家遇到的障碍不同 """
        print('{} the Frog encounters {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Bug:
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t----Frog World -----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(
            self, obstacle, obstacle.action()))


class Ork:
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kill it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    """ 抽象工厂，根据不同的玩家类型创建不同的角色和障碍 (游戏环境)
    这里可以根据年龄判断，成年人返回『巫师』游戏，小孩返回『青蛙过河』游戏"""
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)
2: The Builder Pattern(构造模式: 控制复杂对象的构造)
当对象需要多个部分组合起来一步步创建，并且创建和表示分离的时候。可以这么理解，你要买电脑，工厂模式直接返回一个你需要型号的电脑，但是构造模式允许你自定义电脑各种配置类型，组装完成后给你。这个过程你可以传入builder从而自定义创建的方式。
# factory pattern
MINI14 = '1.4GHz Mac mini'


class AppleFactory:

    class MacMini14:
        def __init__(self):
            self.memory = 4  # in gigabytes
            self.hdd = 500  # in gigabytes
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = ('Model: {}'.format(MINI14),
                    'Memory: {}GB'.format(self.memory),
                    'Hard Disk: {}GB'.format(self.hdd),
                    'Graphics Card: {}'.format(self.gpu))
            return '\n'.join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        else:
            print("I don't know how to build {}".format(model))


# 使用工厂
afac = AppleFactory()
mac_mini = afac.build_computer(MINI14)
print(mac_mini)


# builder模式


class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None      # in gigabytes
        self.hdd = None         # in gigabytes
        self.gpu = None

    def __str__(self):
        info = ('Memory: {}GB'.format(self.memory),
                'Hard Disk: {}GB'.format(self.hdd),
                'Graphics Card: {}'.format(self.gpu))
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer('AG23385193')

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        [step for step in (self.builder.configure_memory(memory),
                        self.builder.configure_hdd(hdd),
                        self.builder.configure_gpu(gpu))]

    @property
    def computer(self):
        return self.builder.computer

# 使用buidler，可以创建多个builder类实现不同的组装方式
engineer = HardwareEngineer()
engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
computer = engineer.computer
print(computer)
3:The Prototype Pattern(原型模式:解决对象拷贝问题)
这是创建模式中的最后一个，用来克隆一个对象，有点像生物学中的有丝分裂。我们可以使用python内置的copy模块实现。拷贝分为深拷贝和浅拷贝，深拷贝会递归复制并创建新对象，而浅拷贝会利用引用指向同一个对象.深拷贝的优点是对象之间互不影响，但是会耗费资源，创建比较耗时；如果不会修改对象可以使用浅拷贝，更加节省资源和创建时间。
	• "A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
	• A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."
import copy
from collections import OrderedDict

class Book:
    def __init__(self, name, authors, price, **rest):
        '''Examples of rest: publisher, length, tags, publication
        date'''
        self.name = name
        self.authors = authors
        self.price = price      # in US dollars
        self.__dict__.update(rest)

    def __str__(self):
        mylist = []
        ordered = OrderedDict(sorted(self.__dict__.items()))
        for i in ordered.keys():
            mylist.append('{}: {}'.format(i, ordered[i]))
            if i == 'price':
                mylist.append('$')
            mylist.append('\n')
        return ''.join(mylist)


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, identifier, obj):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attr):
        """ 实现对象拷贝 """
        found = self.objects.get(identifier)
        if not found:
            raise ValueError('Incorrect object identifier: {}'.format(identifier))
        obj = copy.deepcopy(found)
        obj.__dict__.update(attr)    # 实现拷贝时自定义更新
        return obj


def main():
    b1 = Book('The C Programming Language', ('Brian W. Kernighan', 'Dennis M.Ritchie'),
            price=118, publisher='Prentice Hall', length=228, publication_date='1978-02-22',
            tags=('C', 'programming', 'algorithms', 'data structures'))

    prototype = Prototype()
    cid = 'k&r-first'
    prototype.register(cid, b1)
    b2 = prototype.clone(cid, name='The C Programming Language (ANSI)', price=48.99, length=274,
                        publication_date='1988-04-01', edition=2)
    for i in (b1, b2):
        print(i)
        print("ID b1 : {} != ID b2 : {}".format(id(b1), id(b2)))
4: The Adapter Pattern(适配器模式: 解决接口不兼容问题)
开始介绍结构型设计模式，结构型设计模式通过组合对象来实现新功能。适配器模式通过引入间接层来实现不兼容接口之间的适配。现实中最好的例子就是手机充电口，不同型号安卓手机都可以用同样的充电线充电。在python中可以通过继承实现适配，也可以通过使用class的__dict__属性。 开闭原则：适配器模式和OOP中的开闭原则关系密切，开闭原则强调对扩展开放，对修改关闭。通过适配器模式我们可以通过创建适配器模式在不修改原有类代码的情况下实现新的功能。
class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        """ call by client code """
        return 'execute a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electroinc song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} human'.format(self.name)

    def speak(self):
        return 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        """ 不使用继承，使用__dict__属性实现适配器模式 """
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


# 适配器使用示例
def main():
    objs = [Computer('Asus')]
    synth = Synthesizer('moog')
    objs.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Wnn')
    objs.append(Adapter(human, dict(execute=human.speak)))

    for o in objs:
        # 用统一的execute适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
        print('{} {}'.format(str(o), o.execute()))


if __name__ == "__main__":
    main()
5: The Decorator Pattern(装饰器模式： 无需子类化实现扩展对象功能问题)
通常给一个对象添加新功能有三种方式：
	• 直接给对象所属的类添加方法。
	• 使用『组合』
	• 使用『继承』，优先使用组合而非继承。 装饰器模式提供了第四种选择，通过动态改变对象扩展对象功能。其他编程语言通常使用继承实现装饰器装饰器模式，而python内置了装饰器。装饰器有很多用途，比如数据校验，事务处理，缓存，日志等。比如用装饰器实现一个简单的缓存，python3.5自带了functools.lru_cache
from functools import wraps

def memoize(fn):
    known = dict()

    @wraps(fn)
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]
    return memoizer


@memoize
def fibonacci(n):
    assert(n >= 0), 'n must be >= 0'
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)
6: The Facade Pattern(外观模式: 简化复杂对象的访问问题)
外观模式用来简化复杂系统的访问。通过简化的接口只访问需要的部分，隐藏系统复杂性。想象一下公司接线员，虽然公司内部运行机制比较复杂，但是接线员可以迅速帮你解决特定问题。 我们以实现个简单的操作系统示例说明外观模式：
from abc import ABCMeta, abstractmethod
from enum import Enum

State = Enum('State', 'new running sleeping restart zombie')


class Server(metaclass=ABCMeta):
    """ 抽象基类 """
    @abstractmethod
    def __init__(self):
        pass

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        '''actions required for initializing the file server'''
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''actions required for booting the file server'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''actions required for killing the file server'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        '''check validity of permissions, user rights, etc.'''
        print("trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))

class ProcessServer(Server):
    def __init__(self):
        '''actions required for initializing the process server'''
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print('booting the {}'.format(self))
        '''actions required for booting the process server'''
        self.state = State.running

    def kill(self, restart=True):
        print('Killing {}'.format(self))
        '''actions required for killing the process server'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        '''check user rights, generate PID, etc.'''
        print("trying to create the process '{}' for user '{}'".format(name, user))


class OperatingSystem:
    ''' 实现外观模式，外部使用的代码不必知道 FileServer 和 ProcessServer的
    内部机制，只需要通过 OperatingSystem类调用'''
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        """ 被客户端代码使用 """
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)

def main():
    os = OperatingSystem()
    os.start()
    os.create_file('foo', 'hello', '-rw-r-r')
    os.create_process('bar', 'ls /tmp')

main()
7: The Flyweight Pattern(享元模式: 实现对象复用从而改善资源使用）
Flyweight design pattern is a technique used to minimize memory usage and improve performance by introducing data sharing between similar objects.
OOP编程中容易出现对象创建带来的性能和内存占用问题，需要满足以下条件：
	• 需要使用大量对象(python里我们可以用__slots__节省内存占用)
	• 对象太多难以存储或解析大量对象。
	• 对象识别不是特别重要，共享对象中对象比较会失败。
# 使用对象池技术实现享元模式
import random
from enum import Enum
TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:
    pool = dict()

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if obj is None:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30    # in years
    min_point, max_point = 0, 100
    tree_counter = 0

    for _ in range(10):
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                rnd.randint(min_point, max_point),
                rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(3):
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                rnd.randint(min_point, max_point),
                rnd.randint(min_point, max_point))
        tree_counter += 1

    for _ in range(5):
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                rnd.randint(min_point, max_point),
                rnd.randint(min_point, max_point))
        tree_counter += 1
    print('trees rendered: {}'.format(tree_counter))
    print('trees actually created: {}'.format(len(Tree.pool)))
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print('{} == {}? {}'.format(id(t4), id(t5), id(t4) == id(t5)))
    print('{} == {}? {}'.format(id(t5), id(t6), id(t5) == id(t6)))


if __name__ == '__main__':
    main()
8: The Model-View-Controller Pattern(mvc模式：解耦展示逻辑和业务逻辑)
When using MVC, make sure that you creating smart models (core functionality), thin controllers (functionality required for the communication between the view and the controller), and dumb views (representation and minimal processing).
MVC模式既是一种设计模式，也是软件架构模式。比如流行的django框架就是mvc(MTV)模式。Model层负责和数据库交互，View层负责展现逻辑，Controller层负责粘合Model和View层，将各个部分解耦，使代码更易扩展和维护。
quotes = ('A man is not complete until he is married. Then he is finished.',
        'As I said before, I never repeat myself.',
        'Behind a successful man is an exhausted woman.',
        'Black holes really suck...', 'Facts are stubborn things.')


class QuoteModel:
    def get_quote(self, n):
        try:
            return quotes[n]
        except IndexError:
            return 'Not found'


class QuoteTerminalView:

    def show(self, quote):
        print('And the quote is: "{}"'.format(quote))

    def error(self, msg):
        print('Error: {}'.format(msg))

    def select_quote(self):
        return input('Which quote number would you like to see? ')



class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)
            except ValueError:
                self.view.error("Incorrect index '{}'".format(n))
            else:
                valid_input = True
                quote = self.model.get_quote(n)
                self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()
9: The Proxy Pattern(代理模式：通过一层间接保护层实现更安全的接口访问）
在访问真正的对象之前做一些操作。有四种常用的代理类型:
	• A remote proxy.使得访问远程对象就像本地访问一样，例如网络服务器。隐藏复杂性，使得访问本地远程统一。比如ORM
	• A virtual proxy。用来实现延迟访问，比如一些需要复杂计算的对象，python里可以实现lazy_property，性能改善
	• A protection/protective proxy. 控制敏感对象的访问，加上一层保护层，实现安全控制
	• A smart(reference) proxy. 访问对象时加上一层额外操作，例如引用计数和线程安全检查。weakref.proxy()
代理模式的功能还是很强大的，先来看看使用描述符实现LazyProperty，在对象创建以后第一次访问才会真正生成
class LazyProperty:
    """ 用描述符实现延迟加载的属性 """
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):    # 构造函数里没有初始化，第一次访问才会被调用
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 模拟一个耗时计算
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 访问LazyProperty, resource里的print语句只执行一次，实现了延迟加载和一次执行
    print(t.resource)
    print(t.resource)


main()
再看那个用代理实现安全控制的例子，我们给SensitiveInfo里的add操作加上密钥验证，例子也很简单
class SensitiveInfo:
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


class Info:
    '''protection proxy to SensitiveInfo'''
    def __init__(self):
        self.protected = SensitiveInfo()
        # 为了方便示例这里直接写死在代码里，为了安全不应该这么做
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        """ 给add操作加上密钥验证，保护add操作"""
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))
main()
上面这个示例有几个缺点
	1. SensitiveInfo可以被直接实例化使用，绕过Info类，可以考虑使用abc模块避免SensitiveInfo被直接实例化
	2. 密钥直接写死在代码里，应该用安全性较高密钥写到配置或者环境变量里
我们使用抽象基类来修正第一个缺陷，只需要修正类代码而不用改main函数里的使用代码
from abc import ABCMeta, abstractmethod


class SensitiveInfo(metaclass=ABCMeta):
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def add(self, user):
        pass


class Info(SensitiveInfo):
    '''protection proxy to SensitiveInfo'''
    def __init__(self):
        # self.protected = SensitiveInfo()
        super().__init__()
        self.secret = '0xdeadbeef'    # 为了方便示例这里直接写死在代码里

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        """ 给add操作加上密钥验证，保护add操作"""
        sec = input('what is the secret? ')
        self.users.append(user) if sec == self.secret else print("That's wrong!")
10: The Chain of Responsibility Pattern (责任链模式:创建链式对象用来接收广播消息)
The Chain of Responsibility pattern is used when we want to give a chance to multiple objects to satisfy a single request, or when we don't know which object (from a chain of objects) should process a specific request in advance.
开始介绍行为型设计模式，行为型设计模式处理对象之间的交互和算法问题。在责任连模式中，我们把消息发送给一系列对象的首个节点，对象可以选择处理消息或者向下一个对象传递,只有对消息感兴趣的节点处理。用来解耦发送者和接收者。在python里通过dynamic dispatching来实现，以一个事件驱动系统来说明：
class Event:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:

    """Docstring for Widget. """

    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = 'handle_{}'.format(event)
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event):
        print('MainWindow: {}'.format(event))

    def handle_default(self, event):
        print('MainWindow: Default {}'.format(event))


class SendDialog(Widget):
    def handle_paint(self, event):
        print('SendDialog: {}'.format(event))


class MsgText(Widget):
    def handle_down(self, event):
        print('MsgText: {}'.format(event))


def main():
    mw = MainWindow()
    sd = SendDialog(mw)    # parent是mw
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print('\nSending event -{}- to MainWindow'.format(evt))
        mw.handle(evt)
        print('Sending event -{}- to SendDialog'.format(evt))
        sd.handle(evt)
        print('Sending event -{}- to MsgText'.format(evt))
        msg.handle(evt)

if __name__ == "__main__":
    main()
11: The Command Pattern(命令模式：用来给应用添加Undo操作)
命令模式帮助我们把一个操作(undo,redo,copy,paste等)封装成一个对象，通常是创建一个包含Operation所有逻辑和方法的类。 通过命令模式可以控制命令的执行时间和过程，还可以用来组织事务。 用一些文件操作类来说明命令模式的使用
import os

class RenameFile:

    def __init__(self, path_src, path_dest):
        """ 在init里保存一些必要信息，比如undo需要的老的和新的文件名 """
        self.src, self.dest = path_src, path_dest

    def execute(self, verbose=False):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self, verbose=False):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


def delete_file(path, verbose=False):
    if verbose:
        print("deleting file '{}".format(path))
    os.remove(path)


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path, self.txt = path, txt

    def execute(self, verbose=False):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self, verbose=False):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read(), end='')


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()   # 执行undo
        except AttributeError:
            pass

main()
12: The Interpreter Pattern(解释器模式：用来实现Domain Specific Language(DSL))
本章我们实现一个简单的控制大门Gate类的DSL。使用pyparsing来解析我们定义的控制大门的语法命令。 pyparsing自带了很多有用的函数和类帮助我们从文本中抽取需要的信息，比如我们方便地处理c++源文件中的注释:(pip install pyparsing)
>>> text = '// Look out of the yard? What will we see?'
>>> print pp.cppStyleComment.parseString(text)
['// Look out of the yard? What will we see?']
>>> print pp.cppStyleComment.parseString('/* Author: R. J. Gumby */')
['/* Author: R. J. Gumby */']
再比如我们一句话就可以去除C++源码中的注释:
from pyparsing import cppStyleComment
code = """
/* Hello World program */

#include<stdio.h>

main()
{
    printf("Hello World");    // print hello

}
"""
print(cppStyleComment.suppress().transformString(code))
下面实现我们的控制Gate的DSL
from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums

class Gate:
    def __init__(self):
        self.is_open = False

    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


def main():
    # 首先定义我们的DSL格式，我   这里最简单的控制语法就是   "open -> gate"
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)

    gate = Gate()
    cmds = ['open -> gate', 'close -> gate']    # 两个自定义的命令
    open_actions = {'gate': gate.open}
    close_actions = {'gate': gate.close}

    for cmd in cmds:
        print(event.parseString(cmd))    # [['open'], ['gate']]
        cmd, dev = event.parseString(cmd)
        cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
        print(cmd_str, dev_str)
        if 'open' in cmd_str:
            open_actions[dev_str]()
        elif 'close' in cmd_str:
            close_actions[dev_str]()

if __name__ == "__main__":
    main()
这样就实现了一个简单的大门控制语言，不过功能很弱。
13: The Observer Pattern(发布订阅模式：用来处理多个对象之间的发布订阅问题)
如果用过blinker库或者redis的pub，sub，对发布订阅应该会比较熟悉。该模式用在当一个对象的状态变更需要通知其他很多对象的时候，比如rss订阅或者在社交网站上订阅某个频道的更新。事件驱动系统也是一种发布订阅模式，事件作为发布者，监听器作为订阅者，只不过这里多个事件监听器可以监听同一个事件。 我们这里实现一个"Data Formatter"来解释发布订阅模式，一种数据可以有多个格式化Formatter，当数据更新的时候，会通知所有的Formatter格式化新的数据。使用继承来实现。
class Publisher:
    def __init__(self):
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Failed to add : {}').format(observer)

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Failed to remove : {}').format(observer)

    def notify(self):
        [o.notify_by(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(
            type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()    # data 在被合法赋值以后会执行notify


class HexFormatter:
    """ 订阅者 """
    def notify_by(self, publisher):
        print("{}: '{}' has now hex data = {}".format(
            type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:
    """ 订阅者 """
    def notify_by(self, publisher):
        print("{}: '{}' has now bin data = {}".format(
            type(self).__name__, publisher.name, bin(publisher.data)))


if __name__ == "__main__":
    df = DefaultFormatter('test1')
    print(df)
    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)
14: The State Pattern(状态模式：实现有限状态机)
A state machine is an abstract machine that has two key components: states and transitions. A state is the current (active) status of a system. A transition is the switch from one state to another. A state meachine has only one active state at a specific point in the time. 我们通过实现操作系统中进程的生命周期来演示状态模式的使用：
# 先装下pip3 install state_machine
from state_machine import (
acts_as_state_machine, State, Event, before, after, InvalidStateTransition
)


@acts_as_state_machine
class Process:
    # 先来定义状态机的状态 states
    created = State(initial=True)    # 初始状态
    waiting = State()
    running = State()
    terminated = State()
    blocked = State()
    swapped_out_waiting = State()
    swapped_out_blocked = State()

    # 再定义状态机的转移 transitions
    wait = Event(from_states=(created, running, blocked,
                            swapped_out_waiting), to_state=waiting)
    run = Event(from_states=waiting, to_state=running)
    terminate = Event(from_states=running, to_state=terminated)
    block = Event(from_states=(running, swapped_out_blocked),
                to_state=blocked)
    swap_wait = Event(from_states=waiting, to_state=swapped_out_waiting)
    swap_block = Event(from_states=blocked, to_state=swapped_out_blocked)

    def __init__(self, name):
        self.name = name

    # The state_machine module provides us with the @before and @after
    # decorators that can be used to execute actions before or after a
    # transition occurs, respectfully.
    @after('wait')
    def wait_info(self):
        print('{} entered waiting mode'.format(self.name))

    @after('run')
    def run_info(self):
        print('{} is running'.format(self.name))

    @before('terminate')
    def terminate_info(self):
        print('{} terminated'.format(self.name))

    @after('block')
    def block_info(self):
        print('{} is blocked'.format(self.name))

    @after('swap_wait')
    def swap_wait_info(self):
        print('{} is swapped out and waiting'.format(self.name))

    @after('swap_block')
    def swap_block_info(self):
        print('{} is swapped out and blocked'.format(self.name))


def transition(process, event, event_name):
    """
    Args:
        process (Process obj):
        event (Event obj): wait, run, terminate...
        event_name (str): name of event
    """
    try:
        event()
    except InvalidStateTransition:
        print('Error: transition of {} from {} to {} failed'.format(
            process.name, process.current_state, event_name))


def state_info(process):
    """ 当前状态机的状态 """
    print('state of {}: {}'.format(process.name, process.current_state))

if __name__ == "__main__":
    RUNNING = 'running'
    WAITING = 'waiting'
    BLOCKED = 'blocked'
    TERMINATED = 'terminated'
    p1, p2 = Process('process1'), Process('process2')
    [state_info(p) for p in (p1, p2)]

    print()
    transition(p1, p1.wait, WAITING)
    transition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]
    print()
    transition(p1, p1.run, RUNNING)
    transition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]
    print()
    transition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]
    print()
    [transition(p, p.block, BLOCKED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]
    print()
    [transition(p, p.terminate, TERMINATED) for p in (p1, p2)]
    [state_info(p) for p in (p1, p2)]
15: The Strategy Pattern(策略模式：动态选择算法策略)
现实中往往解决问题的方式不止一种，我们可能需要根据问题的特征选择最优的实现策略，以排序算法为例子，挑选一个合适的排序算法的时候，需要考虑待排序数组的以下特征：
	• 元素个数。算法输入规模，大部分排序算法在输入规模很小的时候效率相差不大，只有一部分nlogn平均时间复杂度的适合排序大规模。
	• 最好/平均/最坏时间复杂度.这个往往是挑选排序算法时候优先考虑的。
	• 空间复杂度。是不是原地排序(inplace),需要额外的空间吗？在内存限制苛刻的时候就需要考虑
	• 稳定性。排序算法是稳定的吗？稳定是指相同大小的值排序后保持相对顺序。
	• 实现复杂度。算法是否容易实现，其他大致相同的情况下，优先考虑易维护的代码。
策略模式允许我们根据待处理数据的特征灵活选用当前特征下最优的实现，比如常见库的排序算法一般都是混合了多种排序算法的实现，python使用的是Tim Peters在2002年设计的结合了合并排序和插入排序的Timsort. 函数在python里是一等公民，可以简化策略模式的实现。
def f1(seq):
    pass

def f2(seq):
    pass

def f(seq):
    if len(seq) >= threshold_value:    # 大于某个阈值
        f1(seq)    # 在数量较多时候具有良好的效率
    else:
        f2(seq)
16: The Template Pattern(模板模式：抽象出算法公共部分从而实现代码复用)
Don't repeat yourself. 模板模式中，我们可以把代码中重复的部分抽出来作为一个新的函数，把可变的部分作为函数参数，从而消除代码冗余。实际上这种模式在代码重构的时候是经常使用的 ，使用一个有意思的例子来说明下，请安装pip install cowpy，真有人闲的*疼写这个玩意
from cowpy import cow


def dots_style(msg):
    msg = msg.capitalize()
    msg = '.' * 10 + msg + '.' * 10
    return msg


def admire_style(msg):
    msg = msg.upper()
    return '!'.join(msg)


def cow_style(msg):
    msg = cow.milk_random_cow(msg)
    return msg


def generate_banner(msg, style=dots_style):
    print('-- start of banner --')
    print(style(msg))
    print('-- end of banner --\n\n')


def main():
    msg = 'happy coding'
    [generate_banner(msg, style) for style in (dots_style, admire_style,
                                            cow_style)]

if __name__ == "__main__":
    main()


"""
-- start of banner --
..........Happy coding..........
-- end of banner --


-- start of banner --
H!A!P!P!Y! !C!O!D!I!N!G
-- end of banner --


-- start of banner --
______________
< happy coding >
--------------
    o
    o
    ^__^         /
    (**)\_______/  _________
    (__)\       )=(  ____|_ \_____
U    ||----w |  \ \     \_____ |
        ||     ||   ||           ||
-- end of banner --
"""
单例模式: 使得一个类最多生成一个实例。
Design ptterns are discoverd, not invented. - Alex Martelli
很奇怪，本书讲完了都没有讲到单例模式。python的单例模式有各种实现，元类、装饰器等，但是还有一种说法：
I don't really see the need, as a module with functions (and not a class) would serve well as a singleton. All its variables would be bound to the module, which could not be instantiated repeatedly anyway. If you do wish to use a class, there is no way of creating private classes or private constructors in Python, so you can't protect against multiple instantiations, other than just via convention in use of your API. I would still just put methods in a module, and consider the module as the singleton.
也就是说，实际上，python中，如果我们只用一个实例，直接这么写就行
# some module.py
class SingletonClass:
    pass

# 在别处我们想用这个实例都直接使用 module.single_instance 这个实例就好。
# 这是最简单也是最直观的一种方式,嗯，直接导入这个实例用，而不是导入class，简单粗暴
single_instance = SingletonClass()
Is there a simple, elegant way to define singletons in Python? [closed]
其他实现：
# http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
class BaseClass:
    pass


# 装饰器实现
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass(BaseClass):
    pass


class Singleton(object):
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class MyClass(Singleton, BaseClass):
pass


# 元类实现
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python2
class MyClass(BaseClass):
    __metaclass__ = Singleton

# Python3
class MyClass(BaseClass, metaclass=Singleton):
    pass
面向过程与面向对象
设计模式讲完了，来看看python中OOP的相关东西。
	• 过程式: 基本都是一个个函数(function)来实现功能，你给我一些参数，我对参数做出各种操作，返回需要的结果。
	• 面向对象：把资源抽象成一个类，数据(data)和方法(method)的集合。在构造函数中进行数据属性的初始化，在方法中进行对象数据的各种操作。
哪种方式更好这个我暂时没有定论，编程规范也不会说强制你使用哪种风格。编码中往往没有绝对正确的，只有相对更优的，如果不好定论，那就一致，易读，易用，易维护的风格优先。一般来说，能用函数实现的优先使用函数，相比类更简单易维护。如果多个过程共享一些状态（操作+数据），这时候使用类就比较适合。使用类的时候尽量保持继承层级简单，如果同样可以完成功能，优先使用组合而非继承。
python中的抽象基类
在python中我们可以使用内置的abc(abstract base class)模块来实现抽象基类。什么时候需要一个抽象基类呢？
	• 抽象基类是没法被实例化的。
	• 抽象基类中定义抽象方法强制子类去实现。
# 为了实现这两个特性，我们可以这么写
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

    # Oh no, we forgot to override bar()...
    # def bar(self):
    #     return "bar() called"
但是这么写依然可以实例化Base，python2.6以后引入了abc模块帮助我们实现这个功能。
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # We forget to declare bar() again...
使用这种方式如果没有在子类里实现bar方法你是没有办法实例化子类的。
《Abstract Base Classes in Python》
《http://stackoverflow.com/questions/3570796/why-use-abstract-base-classes-in-python》
《https://docs.python.org/2/library/abc.html》
python中的Mixin
Mixin是为了给一个类扩充功能用的，它也没法被实例化。我们可以在Mixin类里实现一些方法给类扩充功能。你可能会问了，那为啥不直接写在类里头，比如用@staticmethod方法？我的理解是这样的，为了『高内聚』。如果你用过pylint检测代码，你会发现你在写类的一个方法时，如果在写一个method时没有使用到任何self里的东西，pylint会给提示『R0201 Method could be a function [pylint]』，意思是这个方法可以可以单独写成一个函数，不必要写在类里。也就是说，只有一个类里实现的方法都是使用了self里的数据时才能成为高内聚的（我不知道我这样理解对不对）。例子：flask_login插件有个UserMixin给定义的用户类实现登录功能。
