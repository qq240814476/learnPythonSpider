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