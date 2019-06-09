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