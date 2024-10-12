- 已剪辑自: https://zhuanlan.zhihu.com/p/31700225
- Patterns mean "I have run out of language." - Rich Hickey
- python不像java中比较强调设计模式(编程套路)，动态语言也内置了像是装饰器、迭代器等模式.
- 另外python中的『一切皆对象』、鸭子类型等也导致python中实现的设计模式和其他语言有些差别。
- 根据YAGNI(you aren't gonna need it)和KISS(Keep it simple sutpid)原则，如果能用简单易懂的方式实现，最好不要滥用设计模式以免增加复杂度和维护难度。
- 本博客是《Mastering Python Design Patterns》的读书笔记，涵盖大部分设计模式(力求pythonic实现)，有兴趣可以参考下，代码示例版本为python3.5.2。

1. The Factory Pattern (工厂模式：解决对象创建问题)
   先来看三种创建模式中的第一种工厂模式。
   解释：处理对象创建，客户端可以申请一个对象而不用知道对象被哪个class创建。可以方便地解耦对象的使用和创建。有两种实现，工厂方法和抽象工厂。

   Factory Method (工厂方法)：执行单独的函数，通过传参提供需要的对象的信息。通过一个demo看看例子:

   ```python
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
   ```

   Abstract Factory (抽象工厂：解决复杂对象创建问题)
   工厂方法适合对象种类较少的情况，如果有多种不同类型对象需要创建，使用抽象工厂模式。以实现一个游戏的例子说明，在一个抽象工厂类里实现多个关联对象的创建：

   ```python
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
       这里可以根据年龄判断，成年人返回『巫师』游戏，小孩返回『青蛙过河』游戏 """
       def __init__(self, factory):
           self.hero = factory.make_character()
           self.obstacle = factory.make_obstacle()

       def play(self):
           self.hero.interact_with(self.obstacle)
   ```
