class LinkedListNode:
  def __init__(self, value):
    self.value = value #értéke
    self.pointer=None #köv mutató, ami megmutatja hogy hol a következő lista elem

class LinkedList: #Egyszeresen láncolt lista definiálása
  def __init__(self):
    self.pointer=None
    
  def insert_at_start(self, value): #Lista elejébe való beszúrás
    newnode = LinkedListNode(value)
    newnode.pointer=self.pointer
    self.pointer=newnode