from typing import Iterable, Any
from .errors import StackEmptyException, QueueEmptyException

__all__ = [
  "Queue", "Stack"
]

def foreach(function, iterable: Iterable):
    for element in iterable:
        function(element)

class Queue(list):
  def __init__(self, _: Iterable = []):
    super(Queue, self).__init__(_)
    self._representation = []

  def __getattribute__(self, name):
    if name in ['append', 'index', 'remove']:
      raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    return super(list, self).__getattribute__(name)

  def foreach(self, function):
    foreach(function, self)

  def enqueue(self, item: Any):
    """Add an item to the beginning of the queue."""
    self.insert(0, item)
    self._representation.insert(0, item)

    return self

  def dequeue(self):
    """Removes the topmost item in the queue and returns it."""
    if(len(self) == 0 or len(self._representation) == 0):
      raise QueueEmptyException
    self._representation.pop(len(self) - 1)
    return self.pop(len(self) - 1)

  def peek(self):
    """Returns the topmost item in the queue without removing it."""
    if(len(self) == 0):
      raise QueueEmptyException
    return self[len(self) - 1]

  @property
  def empty(self):
    """A boolean property indicating whether the queue is empty or not."""
    return len(self) == 0

  def __iter__(self):
    for i in self.__reversed__():
      yield i

  def extend(self, iterable: Iterable):
    for i in iterable:
      self.enqueue(i)

  def __str__(self):
    return f"<Queue {self._representation}>"

  @classmethod
  def from_dict(cls):
    pass

class Stack(list):
  def __init__(self, _: Iterable = []):
    super(Stack, self).__init__(_)
    self._representation = _

  def __getattribute__(self, name):
    if name in ['append', 'index', 'remove']:
      raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
    return super(list, self).__getattribute__(name)

  def foreach(self, function):
    foreach(function, self)

  def push(self, item: Any):
    """Add an item to the end of the stack."""
    self.insert(len(self), item)
    self._representation.append(item)

    return self

  def pop(self):
    """Removes the last added item in the list and returns it."""
    if(len(self) == 0 or len(self._representation) == 0):
      raise StackEmptyException
    self._representation.pop(len(self) - 1)
    return self.pop(len(self) - 1)

  def peek(self):
    """Returns the topmost item in the stack without removing it."""
    if(len(self) == 0):
      raise StackEmptyException
    return self[len(self) - 1]

  @property
  def empty(self):
    """A boolean property indicating whether the stack is empty or not."""
    return len(self) == 0

  def search(self, o: Any) -> int:
    """Returns the 1-based position where an object is on this stack. If the object o occurs as an item in this stack, this method returns the distance from the top of the stack of the occurrence nearest the top of the stack; the topmost item on the stack is considered to be at distance 1. The equals method is used to compare o to the items in this stack."""

    index = 0

    for i in self.__reversed__():
      index += 1
      if o == i:
        return index

    return -1

  def __iter__(self):
    for i in self.__reversed__():
      yield i

  def __str__(self):
    return f"<Stack {self._representation}>"

  def extend(self, iterable: Iterable):
    for i in iterable:
      self.push(i)