""" Egyszeresen lancol lista adatstrukturaja """
class LinkedListNode:
    def __init__(self, value):
        """ erteke """
        self.value = value
        """ köv mutato, ami megmutatja hogy hol a következo lista elem """
        self.pointer=None 

class LinkedList:
    """ Egyszeresen lancolt lista definialasa """
    def __init__(self):
        self.pointer=None
    """ Lista elejebe valo beszuras """
    def insert_at_start(self, value):
        newnode = LinkedListNode(value)
        newnode.pointer=self.pointer
        self.pointer=newnode
