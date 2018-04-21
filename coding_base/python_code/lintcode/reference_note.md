### strting转换
.isdigit()

### ord函数
ord是unicode ordinal的缩写,即编号
ord("0")    48
ord("1")    49
ord("9")    57

### 清理空格
.strip()
.rstript()
.lstript()
.strip(' \t\n\r')

## 循环
for counter, option in enumerate(options):

## 数字操作
import math
向上取整 math.ceil
向下取整 math.floor
四舍五入 round
这三个的返回结果都是浮点型

## list操作
list.append(obj)-------------------向列表中添加一个对象obj 
list.count(obj)---------------------返回一个对象obj在列表中出现的次数 
list.extend(seq)--------------------把序列seq的内容添加到列表中 
list.index(obj,i=0,j=len(list))------返回list[k]==obj的k值，并且k的范围在 
                                                       i<=k<J；否则引发ValueError异常。 
list.insert(index,obj)---------------在索引量为index的位置插入对象obj。 

list.remove(obj)-------------------从列表中删除对象obj 
list.reverse()-----------------------对列表进行倒序 
list.sort(func=None, key=None,reverse=False)
--------以指定的方式排序列表中的成员，如果func和key参数指定， 
                                                      则按照指定的方式比较各个元素，如果reverser标志被设置为True， 
                                                      则列表以反序排列。 
- 通过下标删除元素
del a[-1]
list.pop(index=-1)      删除并返回指定位置的对象，默认是最后一个对象 

## 字典操作
 - 删除元素
dict.pop(key)和del dict[key]

 - 获取元素
获取不存在的键的值就会触发的一个KeyError异常
>>> info = dict(name= 'cold', blog='www.linuxzen.com')
>>> info.get('name')
'cold'
>>> info.get('blogname')
None
>>> info.get('blogname', 'linuxzen')
'linuxzen'
我们看到使用get方法获取不存在的键值的时候不会触发异常,同时get方法接收两个参数,当不存在该键的时候就会返回第二个参数的值 我们可以看到使用get更加的优雅

- 遍历字典
for k,v in d.items()