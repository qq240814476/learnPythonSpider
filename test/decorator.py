# 装饰器练习
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
import functools
import datetime

def dec(func):
  @functools.wraps(func)
  def wrapper(*arg, **kw):
    print('begin call %s' % func.__name__)
    @functools.wraps(func)
    def end(*arg, **kw):
      func(*arg, **kw)
      print('end call %s' % func.__name__)
    return end(*arg, **kw)
  return wrapper

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