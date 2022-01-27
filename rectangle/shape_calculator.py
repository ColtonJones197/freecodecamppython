import math

class Rectangle:
  def __init__(self, width, height):
    self.width, self.height = width, height
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return self.height * self.width
  def get_perimeter(self):
    return self.height * 2 + self.width * 2
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    output = ''
    for i in range(0, self.height):
      output += '*' * self.width + '\n'
    return output
  def get_amount_inside(self, shape):
    times_it_fits_height = math.floor(self.height / shape.height)
    times_it_fits_width = math.floor(self.width / shape.width)
    return times_it_fits_width * times_it_fits_height

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):
  def __init__(self, length):
    self.width, self.height = length, length
  def set_side(self, length):
    self.width, self.height = length, length
  def set_width(self, length):
    self.width, self.height = length, length
  def set_height(self, length):
    self.width, self.height = length, length
  def __str__(self):
    return f'Square(side={self.width})'
