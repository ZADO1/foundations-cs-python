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
        self.size +=1    # increase size


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

    def SeafchAndDelete(self,key):
        # https://www.geeksforgeeks.org/python-program-for-deleting-a-node-in-a-linked-list/
        curr = self.head

        # If the  head node containe the data or key  simply we change the heade to the curr.next  means the next node
        if (curr is not None):
            if (curr.data == key):
                self.head = curr.next
                curr = None
                return
        while (curr is not None):
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
            self.size -=1   # decrease size
            print(f"Node remove with value: {key} ")
        if (curr == None):   # if current == none is empty
            return

        prev.next = curr.next
        curr = None


# def isPalindrome(s):
#   return s == s[::-1]
# user_input = input("Enter a string: ")
# result = isPalindrome(user_input)
# if result:
#   print(f"{user_input} its a palindrome.")
# else:
#   print(f"{user_input} not a palindrome.")
#

# create class stack |_| and i define 3 func
class Stack:
  def __init__(self):
      self.items = []

  def isEmpty(self):
      return self.items == []

  def push(self, data):
      self.items.append(data)

  def pop(self):
      self.isEmpty()
      return self.items.pop()

def ispalindrome():
    a = input("Enter a word: ")
    s = Stack()
    for i in a:
        s.push(i)
    reversed_word = ""

    while not s.isEmpty():
        reversed_word += s.pop()
    if reversed_word == a:
        print("The word is a palindrome")
    else:
        print("It's not a palindrome")
        print("Original word:", a)
        print("Reversed word:", reversed_word)

class Student:
    #constructor
    def __int__(self,name,midterm,final_grade,good_personality):
        self.name = name
        self.midterm = midterm
        self.finale_grade = final_grade
        self.good_personality = good_personality
class Nodee:
    # create node data (student) and next = none
    def __int__(self,student):
        self.student = student
        self.next = None

class PriorityQueue:
    def __init__(self):
      self.head = None
      self.size = 0

    def enqueue(self, student):
        node = Nodee(student)

        if self.size == 0:
            # If the list is empty, set the new node as the head
            self.head = node
            self.size += 1
        else:
            curr = self.head
            prev = None

            while curr:
                if node.student.good_personality and not curr.student.good_personality:
                    node.next = curr
                    if not prev:
                        self.head = node
                    else:
                        prev.next = node
                    self.size += 1
                    return
                elif curr.student.good_personality and not node.student.good_personality:
                    node.next = curr.next
                    curr.next = node
                    self.size += 1
                    return
                else:
                    if (node.student.final_grade > curr.student.final_grade or(node.student.final_grade == curr.student.final_grade and  node.student.midterm_grade > curr.student.midterm_grade)):
                        node.next = curr
                        if not prev:
                            self.head = node
                        else:
                            prev.next = node
                        self.size += 1
                        return
                    elif node.student.final_grade < curr.student.final_grade or (node.student.final_grade == curr.student.final_grade  and node.student.midterm_grade < curr.student.midterm_grade):
                        node.next = curr.next
                        curr.next = node
                        self.size += 1
                        return
                    else:

                        if node.student.midterm_grade > curr.student.midterm_grade:
                            node.next = curr
                            if not prev:
                                self.head = node
                            else:
                                prev.next = node
                                self.size += 1
                            return
                        elif node.student.midterm_grade < curr.student.midterm_grade:
                            node.next = curr.next
                            curr.next = node
                            self.size += 1
                            return

                prev = curr
                curr = curr.next
            prev.next = node
            self.size += 1

    def Dequeue(self):
        if self.size == 0:  # check if the queu is empty
            print(" no students ")
        elif self.size == 1:
            print(f" {self.head.student.name} enter the interview ")
            self.head = None
            self.size -= 1  # decrease sizze of queue and head equal none because the queue will be empty
        else:
            print(f" {self.head.student.name}enter the interview")
            current = self.head  # create pointer
            self.head = self.head.next  # change head to the next node
            current.next = None
            self.size -= 1

