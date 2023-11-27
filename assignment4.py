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
def Menu():
    print("1. Singly LinkedList\n"+
         "2. Check if Palindrome\n"+
         "3. Priority Queue\n"+
         "4. Evaluate an Infix Expression\n"+
         "5. Graph\n"+
         "6. Exit")



def linkedlistMenu():
    print("a.Add Node\n"+
          "b.Display Nodes\n"+
          "c.Search for & Delete Node\n"+
          "d.Return to main menu")

def displayMenuStudent():
    print("a. Add a student\n"+
           "b. Interview a student\n"+
           "c. Return to main menu")

def displayMenuGraph():
    print("a. Add vertex\n"
          + "b. Add edge\n"
          + "c. Remove vertex\n"
          + "d. Remove edge\n"
          + "e. Display vertices with a degree of X or more.\n"
          + "f. Return to main menu")


# linkedlist consists of nodes  we need to create class node
# node containe data  and next we put next equal to none by default
class Node:
    def __init__(self,data):
        self.data= data
        self.next = None


# we need to define class of linked list ,every linkedlist has a head and tail
# we put head  and tail equal none because when w create linkedlist will be empty
class Linkedlist:
    def __init__(self):
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
            newNode.next = None
        self.size +=1    # increase size


    def DisplayNodes(self):

        if self.size == 0:
            print("linkedlist is empty")
            return
        # i create a pointer curr and we start from head to print data
        curr = self.head
        while curr:
            print(curr.data , end=" --> ")
            curr = curr.next   # here we change the pointer to the next node
        print(".....")


    def searchAndRemove(self, key):
        if self.size == 0:  #if the linked list isempty
            print("Cant search and delete the Node since no Nodes yet .")
            return
        curr = self.head
        prev = None
        while curr:
            if curr.data == key:
                if curr == self.head:  #If the  head node containe the data or key  simply we change the head to the curr.next  means the next node
                    self.head = curr.next
                    if curr == self.tail:
                        self.tail = None
                else:
                    prev.next = curr.next
                    if curr == self.tail:    #the opposite #if the tail node cotaine the key we change pointer tail to prev
                        self.tail = prev
                self.size -= 1        # decrease size
                print(f" {key} deleted")
                return
            prev = curr
            curr = curr.next
        print(f"{key} not in the linkedlist")
def inputNumeric(numeric_value):
    try:
        if "." in numeric_value or (numeric_value[0] == '-' and "." in numeric_value[1:]):
             numeric_value = float(numeric_value)
        elif numeric_value[0] == '-':
             numeric_value = int(numeric_value)
        else:
          numeric_value = int(numeric_value)
    except ValueError:
            print("Please enter a valid numeric value.")


# def isPalindrome(s):
#   return s == s[::-1]
# user_input = input("Enter a string: ")
# result = isPalindrome(user_input)
# if result:
#   print(f"{user_input} its a palindrome.")
# else:
#   print(f"{user_input} not a palindrome.")
#

# create class stack |_| and i define 3 fun


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
    def __init__(self,name,midterm,final_grade,good_personality):
        self.name = name
        self.midterm = midterm
        self.final_grade = final_grade
        self.good_personality = good_personality
class Nodee:
    # create node data (student) and next = none
    def __init__(self,student):
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

    def AddStudent(self):
        max = 3
        input_name = ""
        midterm_grade = ""
        final_grade = ""
        good_personality = ""
        for attempt in range(1, max + 1):   #the loop stops before reaching max so we add + 1 it includes max
            input_name = input("Enter student name: ")

            if input_name.isalpha():   # https://www.w3schools.com/python/ref_string_isalpha.asp
                break
            else:
                print("Please enter a valid name for the student.")
                if attempt < max:
                    print(f"You have {max - attempt} attempts left")
                else:
                    print("Failed to meet the naming criteria after multiple attempts")
                    return

        for attempt in range(1, max + 1):
            midterm_grade = input("Enter midterm grade: ")

            if midterm_grade.isdigit() and 0 <=int(midterm_grade)<= 100:
                break
            else:
                print("Please enter a valid grade for the student.")
                max +=1
                if attempt < max:
                    print(f"You have {max - attempt} attempts left")
                else:
                    print("Failed to meet the grade criteria after multiple attempts")
                    return

        for attempt in range(1, max + 1):
            final_grade = input("Enter final grade: ")

            if final_grade.isdigit() and 0 <= int(midterm_grade) <= 100:
                break
            else:
                print("Please enter a valid grade for the student.")
                max += 1
                if attempt < max:
                    print(f"You have {max - attempt} attempts left")
                else:
                    print("Failed to meet the grade criteria after multiple attempts")
                    return

        limit = 0
        max_attempts = 3

        while limit < max_attempts:

            good_personality = input("Does this student have a good personality?(Enter 'YES' or 'Y' for yes, 'NO' or 'N' for no):  ".lower())

            if good_personality in ['yes', 'y']:
                good_personality = True
                break
            elif good_personality in ['no', 'n']:
                good_personality = False
                break

            print("Please enter either 'yes'/'y' or 'no'/'n'.")
            limit += 1
            print(f"You have {max_attempts - limit} attempts left")

        new_student = Student(input_name, midterm_grade, final_grade, good_personality)
        self.enqueue(new_student)    #this student is added to a priority queuee.

def calculate(expression):
    def precedence(operator):
        if operator in {'+', '-'}:
            return 1
        elif operator in {'*', '/'}:
            return 2
        return 0

    def apply_operator(operators, numbers):
        operator = operators.pop()
        right_number = numbers.pop()
        left_number = numbers.pop()

        if operator == "+":
            numbers.append(left_number + right_number)
        elif operator == "-":
            numbers.append(left_number - right_number)
        elif operator == "*":
            numbers.append(left_number * right_number)
        elif operator == "/":
            numbers.append(left_number // right_number)

    operators = []
    numbers = []

    i = 0
    while i < len(expression):
        char = expression[i]

        if char.isdigit():
            j = i
            while j < len(expression) and expression[j].isdigit():
                j += 1
            numbers.append(int(expression[i:j]))
            i = j
        elif char in "+-*/":
            while (
                operators
                and operators[-1] in "+-*/"
                and precedence(operators[-1]) >= precedence(char)
            ):
                apply_operator(operators, numbers)
            operators.append(char)
            i += 1
        elif char == "(":
            operators.append(char)
            i += 1
        elif char == ")":
            while operators[-1] != "(":
                apply_operator(operators, numbers)
            operators.pop()
            i += 1
        else:

            i += 1

    while operators:
        apply_operator(operators, numbers)

    return numbers[0]


def infixExpression():
    try:
      expression = input("Enter an infix expression: ")
      result = calculate(expression)
      print("Result:", result)
    except ValueError:
        print("Value error, please check your expression")
    except IndexError:
        print("Index error, please check your expression")


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def removeNode(self, data):
        if self.size == 0:
            return

        current = self.head
        previous = None

        while current and current.data != data:
            previous = current
            current = current.next

        if current:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
            self.size -= 1

    def getElements(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def display_nodes(self):
        temp = self.head
        while temp:
            print(temp.data, end="-->")
            temp = temp.next
        print("None")

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self):
        vertex = input("Enter  vertex: ")
        if vertex.isdigit():
            vertex = int(vertex)
            if vertex not in self.adjacency_list:
                self.adjacency_list[vertex] = LinkedList()
                print(f"Vertex {vertex} added.")
            else:
                print(f"Vertex {vertex}exists")

    def addEdge(self):
        if not self.adjacency_list:
            print("empty graph")
            return

        v1 = input("Enter the first vertex: ")
        v2 = input("Enter the second vertex: ")

        if not (v1.isdigit() and v2.isdigit()):
            print("Please enter valid vertices.")
            return

        v1, v2 = int(v1), int(v2)

        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].add_node(v2)
            self.adjacency_list[v2].add_node(v1)
            print(f"Edge added between vertex {v1} and vertex {v2}.")
        else:
            print(f"One or both vertices do not exist in the graph.")

    def display_vertices(self):
        if not self.adjacency_list:
            print("The graph is empty; there is nothing to display.")
            return

        input_vert = input("Enter the vertex you wish to display and show all vertices greater than it: ")

        if input_vert.isdigit():
            input_vert = int(input_vert)

            if input_vert not in self.adjacency_list:
                print(f"Vertex {input_vert} is not found in the graph.")
                return

            print(f"Vertices greater than or equal to {input_vert}: ", end="")
            for vertex in self.adjacency_list:
                if vertex >= input_vert:
                    print(f"{vertex},", end=" ")
            print()
        else:
            print("Please enter a valid vertex number.")

    def remove_vertex(self):
        if not self.adjacency_list:
            print("The graph is empty")
            return

        vert_input = input("Enter the vertex delete: ")

        if not vert_input.isdigit():
            print("Please enter a valid vertex.")
            return

        vertex = int(vert_input)

        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            print(f"Vertex {vertex} has been removed.")
        else:
            print(f"Vertex {vertex}not found ")

    def remove_edge(self):
        if not self.adjacency_list:
            print("The graph is empty")
            return

        vertex1_input = input("Enter the first vertex: ")
        vertex2_input = input("Enter the second vertex: ")

        if not (vertex1_input.isdigit() and vertex2_input.isdigit()):
            print("Please enter valid vertex numbers.")
            return

        v1 = int(vertex1_input)
        v2= int(vertex2_input)

        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            if (
                    v2 in self.adjacency_list[v1].get_elements()
                    and v1 in self.adjacency_list[v2].get_elements()
            ):
                self.adjacency_list[v1].remove_node(v2)
                self.adjacency_list[v2].remove_node(v1)
                print(f"removed Edge between  {v1} and {v2}.")
            else:
                print(f"no edge between{v1} and  {v2}.")
        elif v1 in self.adjacency_list and v2 not in self.adjacency_list:
            print(f"Can't remove edge since vertex {v2} was not found.")
        elif v2 in self.adjacency_list and v1 not in self.adjacency_list:
            print(f"Can't remove edge since vertex {v1} was not found.")
        else:
            print(f"There is no edge between vertex {v1} and vertex {v2}.")



def main():
    linked_list = Linkedlist()
    priority_queue = PriorityQueue()
    graph = Graph()
    maximum = 0
    choice = ""
    while maximum < 4:
        Menu()
        choice = input("Enter your choice :")
        if choice == "1":
            maximum = 0
            sub_choice = ""
            while sub_choice != "d" and maximum < 4:
                linkedlistMenu()
                sub_choice = input("Enter your choice :").lower()
                if sub_choice == "a":
                    numeric_value = input("Enter a number to add: ")
                    inputNumeric(numeric_value)
                    linked_list.AddNode(numeric_value)
                elif sub_choice == "b":
                    linked_list.DisplayNodes()
                elif sub_choice == "c":
                    input_value = input("Enter Node value to remove :")
                    inputNumeric(input_value)
                    linked_list.searchAndRemove(input_value)
                elif sub_choice == "d":
                    main()
                else:
                    maximum += 1
                    print("Invalid choice, please enter the correct choice.")
                    print(f"You have {4 - maximum} attempts left")
        elif choice == "2":

            ispalindrome()
        elif choice == "3":
             maximum = 0
             student_choice = ""
             while student_choice != 'c' and maximum < 4:
              displayMenuStudent()
              student_choice = input("Enter your choice :").lower()
              if student_choice == "a":
                  priority_queue.AddStudent()
              elif student_choice == "b":
                  priority_queue.Dequeue()
              elif student_choice == "c":
                  main()
              else:
                  maximum += 1
                  print("Invalid choice, please enter the correct choice.")
                  print(f"You have {4 - maximum} attempts left")
        elif choice == "4":
            infixExpression()
        elif choice == "5":
            maximum = 0
            graph_choice = ""
            while graph_choice != 'f' and maximum < 4:
                displayMenuGraph()
                graph_choice = input("Enter your choice :").lower()
                if graph_choice == "a":
                    graph.addVertex()
                elif graph_choice == "b":
                    graph.addEdge()
                elif graph_choice == "c":
                    graph.remove_vertex()
                elif graph_choice == "d":
                    graph.remove_edge()
                elif graph_choice == "e":
                    graph.display_vertices()
                elif graph_choice == "f":
                    main()
                else:
                    maximum += 1
                    print("Invalid choice, please enter the correct choice.")
                    print(f"You have {4 - maximum} attempts left")
        elif choice == "6":
            exit()
        else:
            maximum += 1
            print("Invalid choice")
            print(f"You have {4 - maximum} attempts left")


if __name__ == '__main__':
    main()