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
