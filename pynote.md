## 高级特性

### 切片
```python
l = range(100)
l[10:20]
[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

l[:10:2]
[0, 2, 4, 6, 8]
# 所有数，每5个取一个：
l[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
# 甚至什么都不写，只写[:]就可以原样复制一个list
l[:]
[0, 1, 2, 3, ..., 99]
# tuple切片返回tuple
(0, 1, 2, 3, 4, 5)[:3]
(0, 1, 2)
```

### 迭代
默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()<br/>
Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身<br/>

```python
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
# True

for i, value in enumerate(['A', 'B', 'C']):
  print(i, value)
# 0 A
# 1 B
# 2 C
```

### 列表生成式

```python
[x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]

[m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

[k + '=' + v for k, v in d.items()]
# ['y=B', 'x=A', 'z=C']

y = 123
isinstance(y, str)
# False
```

### 生成器    需要细细研究下
generator
```python

L = [x * x for x in range(10)]
L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
g
<generator object <genexpr> at 0x1022ef630>
```
如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值, 也可以用for循环

```python
# 斐波那锲
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b # 还可以这么写啊   a, b = b, a + b
        n = n + 1
    return 'done'

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 正好复习一下js的Generator，function* 每次yield停止，next()再继续走下去
        a, b = b, a + b
        n = n + 1
    return 'done'
```

```javascript
function* helloWorldGenerator() {
  yield 'hello';
  yield 'world';
  return 'ending';
}

var hw = helloWorldGenerator();

hw.next()
// { value: 'hello', done: false }

hw.next()
// { value: 'world', done: false }

hw.next()
// { value: 'ending', done: true }

hw.next()
// { value: undefined, done: true }
```
js yield <br/>
1. 遇到yield表达式，就暂停执行后面的操作，并将紧跟在yield后面的那个表达式的值，作为返回的对象的value属性值。
2. 下一次调用next方法时，再继续往下执行，直到遇到下一个yield表达式。
3. 如果没有再遇到新的yield表达式，就一直运行到函数结束，直到return语句为止，并将return语句后面的表达式的值，作为返回的对象的value属性值。
4. 如果该函数没有return语句，则返回的对象的value属性值为undefined。

### 迭代器
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。<br/>
凡是可作用于for循环的对象都是Iterable类型；<br/>
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；<br/>
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。<br/>
Python的for循环本质上就是通过不断调用next()函数实现的，例如：<br/>
```python
for x in [1, 2, 3, 4, 5]:
    pass
# 等价于

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```
## 函数式编程
### 匿名函数
关键字<code>lambda</code>表示匿名函数，冒号前面的x表示函数参数。<br/>
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
```python
list(map(Lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### 装饰器
我们要借助Python的@语法，把decorator置于函数的定义处<br/>
把@log放到now()函数的定义处，相当于执行了语句:

```python
now = log(now)
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
import datetime

def dec(func):
  @functools.wraps(func)
  def begin(*arg, **kw):
    print('begin call %s' % func.__name__)
    @functools.wraps(func)
    def end(*arg, **kw):
      func(*arg, **kw)
      print('end call %s' % func.__name__)
    return end(*arg, **kw)
  return begin

@dec
def now():
  print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 思考一下能否写出一个@log的decorator，使它既支持@log 有支持@log('execute')

def autoDecorate(string = ''):
  def mainDec(func):
    @functools.wraps(func)
    def wrapper(*arg, **kw):
      print('call %s' % func.__name__)
      if (len(string) > 0):
        print('附带参数：%s' % string)
      return func(*arg, **kw)
    return wrapper
  return mainDec

@autoDecorate('aaa')
def writeaaa():
  print('执行了write')



@autoDecorate()
def write():
  print('执行了write')

now()
writeaaa()
write()
```

### 偏函数
偏函数就是在原有的函数上面加参数，构造成新的函数   <code>functools.partial</code>
```python
int2 = functools.partial(int, base=2)
# 等价于
kw = { 'base': 2 }
int('10010', **kw)
```

## 作用域
类似<code>__xxx__</code>这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的<code>__author__</code>，<code>__name__</code>就是特殊变量，hello模块定义的文档注释也可以用特殊变量<code>__doc__</code>访问，我们自己的变量一般不要用这种变量名；<br/>
类似<code>_xxx</code>和<code>__xxx</code>这样的函数或变量就是非公开的（private），不应该被直接引用，比如<code>_abc</code>，<code>__abc</code>等；<br/>
之所以我们说，<code>private</code>函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用<code>private</code>函数或变量。<br/>
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）<br/>

```python
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
```

需要注意的是，在Python中，变量名类似<code>__xxx__</code>的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用<code>__name__</code>、<code>__score__</code>这样的变量名。<br/>
有些时候，你会看到以一个下划线开头的实例变量名，比如<code>_name</code>，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。<br/>
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问<code>__name</code>是因为Python解释器对外把<code>__name</code>变量改成了<code>_Student__name</code>，所以，仍然可以通过<code>_Student__name</code>来访问<code>__name</code>变量<br/>

## 面向对象编程
### 继承和多态
python 是动态语言，“叫的像鸭子走路像鸭子那么就是个鸭子”,只需要定义了需要的方法就可以传入进去。

```python
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

### 获取对象信息

```python
type(123)
# <class 'int'>

type(Lambda x: x)==types.LambdaType
# True

type((x for x in range(10)))==types.GeneratorType
# True

type(abs)==types.BuiltinFunctionType
# True

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
a = Animal()
d = Dog()
h = Husky()
isinstance(h, Husky)
# True

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
isinstance([1, 2, 3], (list, tuple))
# True

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
len(dog)
# 100

getattr(obj, 'y')
setattr(obj, 'y', 19
hasattr(obj, 'x')

getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
# 404
```

### 实例属性和类属性
实例属性优先级高于类属性，不推荐重名使用
```python
class Student(object):
    name = 'Student'
s = Student() # 创建实例s
print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
# Student
print(Student.name) # 打印类的name属性
# Student
s.name = 'Michael' # 给实例绑定name属性
print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
# Michael
print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
# Student
del s.name # 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
# Student
```

## 面向对象高级编程
### 使用@property
```python
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score # OK，实际转化为s.get_score()
60
s.score = 9999
Traceback (most recent call last):
ValueError: score must between 0 ~ 100!

# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
  def __init__(self, width = 0, height = 0):
    self.width = width
    self.height = height
  @property
  def width(self):
    return self._width
  @width.setter
  def width(self, value):
    if not isinstance(value, int):
      raise ValueError('width must be int')
    self._width = value
  
  @property
  def height(self):
    return self._height
  @height.setter
  def height(self, value):
    if not isinstance(value, int):
      raise ValueError('height must be int')
    self._height = value
  
  @property
  def resolution(self):
    return self._width * self._height

# test:
s = Screen(1024, 768)
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
```

### 多重继承 MixIn
一个类，继承和混入多个类
> <code>Python</code>自带的很多库也使用了MixIn。举个例子，Python自带了<code>TCPServer</code>和<code>UDPServer</code>这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由<code>ForkingMixIn</code>和<code>ThreadingMixIn</code>提供。通过组合，我们就可以创造出合适的服务来。
