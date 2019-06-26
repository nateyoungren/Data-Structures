"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):

    new_head = ListNode(value) # create new head

    if self.head is None: # check to see if head exists
      self.head = new_head
      self.tail = new_head
      self.length += 1
      return new_head.value

    old_head = self.head # copy current head to old head

    old_head.prev = new_head # set old head previous to ref new head
    new_head.next = old_head # set new head next to ref old head

    self.head = new_head
    self.length += 1

    return new_head.value

  def remove_from_head(self):

    if self.head is None:
      # self.head = self.head

      # self.head = None
      # self.tail = None

      # return self.head.value
      return None

    value = self.head.value

    if self.head.next:
      self.head = self.head.next
    else:
      self.tail = None
      self.head = None

    self.length -= 1

    return value

  def add_to_tail(self, value):
    
    new_tail = ListNode(value)

    if self.head is None:
      self.head = new_tail
      self.tail = new_tail
    else:
      old_tail = self.tail
      old_tail.next = new_tail
      new_tail.prev = old_tail
      self.tail = new_tail

    self.length += 1
    return new_tail.value

  def remove_from_tail(self):

    if self.tail is None:
      return None
    
    old_tail = self.tail
    new_tail = None

    if self.tail.prev:
      new_tail = self.tail.prev
      old_tail.prev = None
      new_tail.next = None
    else:
      self.head = None
      self.tail = None
      self.length -= 1
      return old_tail.value

    self.tail = new_tail
    self.length -= 1
    return old_tail.value

  def move_to_front(self, node):
    
    if self.head is None:
      self.head = node
      self.tail = node
      return node.value

    old_head = self.head

    if node.next and node.prev:
      node.next.prev = node.prev
      node.prev.next = node.next
    elif node.next and node.prev is None:
      self.head = node
      return node.value
    elif node.prev and node.next is None:
      old_tail = node
      new_tail = old_tail.prev
      new_tail.next = None
      self.tail = new_tail

    old_head.prev = node
    node.next = old_head
    node.prev = None
    self.head = node

    return node.value

  def move_to_end(self, node):
    
    if self.tail is None:
      self.tail = node
      self.head = node
      return node.value

    if self.tail is node:
      return node.value

    if self.head is node and self.tail is not node:
      self.head = node.next
      node.next = None
    else:
      node.prev.next, node.next.prev = node.next.prev, node.prev.next

    old_tail = self.tail

    node.prev = old_tail
    node.next = None
    old_tail.next = node
    self.tail = node
    
    return node.value

  def delete(self, node):
    
    if self.head is None:
      return None

    if self.head is node:
      self.head = node.next

    if self.tail is node:
      self.tail = node.prev

    self.length -= 1

    node.delete()

    return node.value
    
  def get_max(self):

    if self.head is None:
      return 0

    current_node = self.head
    max_number = current_node.value

    while current_node:

      if current_node.next:
        current_node = current_node.next

        if current_node.value > max_number:
          max_number = current_node.value

      else:
        current_node = None

    return max_number
