class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.storage.insert(self.size, item)
    self.size += 1
  
  def dequeue(self):
    if not self.storage:
      return None

    element = self.storage[0]

    del self.storage[0]
    self.size -= 1
    return element
    
  def len(self):
    return self.size
