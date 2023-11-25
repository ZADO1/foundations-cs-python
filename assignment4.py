def menu():
    print("1.Singly linkedlist\n"+
          "2.Check if palindrom\n"+
          "3.Priority Queue\n"+
          "4.Evaluate an Infix Expression\n"+
          "5.Graph\n"+
          "6.Exit")


def linkedlistMenu():
    print("a.Add Node\n"+
          "b.Display Nodes\n"+
          "c.Search for & Delete Node\n"+
          "d.Return to main menu")

# we need to define class of linked list ,every linkedlist has a head and tail
# we put head  and tail equal none because when w create linkedlist will be empty
class Linkedlist:
    def __int__(self):
        self.head = None
        self.tail = None
        self.size = 0

# linkedlist consists of nodes  we need to create class node
# node containe data  and next we put next equal to none by default
class Node:
    def __int__(self,data):
        self.data= data
        self.next = None
