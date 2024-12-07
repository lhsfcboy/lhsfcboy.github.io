# 面向对象

## repr 与 str

推荐总是定义__repr__方法
__str__()如果没有定义的话, str()会调用__repr__()

```shell
>>> import datetime
>>> today = datetime.date.today()
>>> str(today)
'2018-04-12'
>>> print(today)
'2018-04-12'
>>> repr(today)
'datetime.date(2018, 4, 12)'
>>> today
datetime.date(2018, 4, 12)
```

## 为class提供比较方法

```python
@total_ordering
class Student:
    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))
```

The class must define one of __lt__(), __le__(), __gt__(), or __ge__().
In addition, the class should supply an __eq__() method.
Python's sort is documented as using only __lt__()
