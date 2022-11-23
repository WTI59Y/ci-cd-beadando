""" Egyszeresen lancol lista adatstrukturaja """
import dataclasses


@dataclasses.dataclass



class LinkedListNode:
    """ Egyszeresen lancolt lista osztaly"""
    def __init__(self, value):
        self.value = value
        self.pointer=None
class LinkedList:
    """ Egyszeresen lancolt lista definialasa """
    def __init__(self):
        self.pointer=None
    def insert_at_start(self, value):
        """ Lista elejebe valo beszuras """
        newnode = LinkedListNode(value)
        newnode.pointer=self.pointer
        self.pointer=newnode
