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



# linkedlist consists of nodes  we need to create class node
# node containe data  and next we put next equal to none by default
class Node:
    def __int__(self,data):
        self.data= data
        self.next = None


# we need to define class of linked list ,every linkedlist has a head and tail
# we put head  and tail equal none because when w create linkedlist will be empty
class Linkedlist:
    def __int__(self):
        self.head = None
        self.tail = None
        self.size = 0
#first add node first we check if the linked list is empty simply we change the head and tail  == newnode
#if the linkedlist not empty  we change the tail.next == new node  and tail.next well be pointer none


    def AddNode(self,data):
        newNode = Node(data)
        if self.size == 0:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.size +=1    # we add one aaal size

    def DisplayNodes(self):

        if self.size == 0:
            print("linkedlist is empty")
            return
        # i create a pointer curr and we start from head to print data
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next   # here we change the pointer to the next node
        print("done")

