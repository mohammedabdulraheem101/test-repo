class Stack:
  def __init__(self, size):      
    self._a = []
    self._top = None
    self._size = size

  def push(self, data):
    if self._top is None:
      ar = []
      ar.append(data)
      self._a = ar
      self._top = 0

    else:
      ar = []
      for i in self._a:
        self.apnd(ar, i)          

      self.apnd(ar, data)
      self._a = ar
      self._top += 1

  def peek(self):
    return self._a[self._top]

  def apnd(self, ar, data):      
    new_ar = [None] * (len(ar) + 1)

    for i in range(len(ar)):
      new_ar[i] = ar[i]

    new_ar[len(ar)] = data

    ar.clear()
    for item in new_ar:
      ar += [item]               


stack = Stack(3)

stack.push(10)
stack.push(20)

print(stack.peek())