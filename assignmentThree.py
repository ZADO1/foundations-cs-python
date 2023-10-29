def get_matrix(rows, col):
    matrix = []
    print(f"Enter number for ({rows}x{col}) : ")
    for i in range(rows):
        row = []
        print(f"Enter number of row {i + 1}")
        number = input().split()
        for j in range(col):
            row.append(int(number[j]))
        matrix.append(row)
    return matrix

print(get_matrix(1,1))

# part2:
def add_Matrices(matrixONE, matrixTwo): # O(n^2)
    result = []
    for i in range(len(matrixONE)):
        row = []
        for z in range(len(matrixONE[0])):
         row.append(matrixONE[i][z] + matrixTwo[i][z])
        result.append(row)
    return result
#
# part3
def convertMatrix_Dictionary(rows, col):  #  O(n^2)
    mat = []
    print(f"Enter the num for {rows},{col}")
    for i in range(rows):
        row = []
        for z in range(col):
           num = input("Enter num :")
           row.append(num)
        mat.append(row)
        print(mat)

# part4 and 5
def display_matrix(matrix):  # O(n)
    for row in matrix:
     print(row)
def dictionary_input():  #O(n)
    dic = {}
    while True:
        element = input("Enter a element or enter 'q' to quit :")
        if element == "q":
            break
        else:
            value = input("Enter a value :")
        dic[element] = value
    dic2 = {}
    for element, value in dic.items():
        if value not in dic2:
            dic2[value] = element
        else:
           dic2[value].append(element)
    print("first  dic :")
    print(dic)
    print("invert dic :")
    print(dic2)

#     part 6
def rotation_matrix(matone, mat2):  # O(n^2)
    if len(matone) != len(mat2[0]) or len(matone[0]) != len(mat2):
        return False
    for i in range(len(matone)):  # O(n)
        for z in range(len(matone[0])):  # O(n)
           if matone[i][z] != mat2[z][i]:  # O(1)
               return False
    return True

# part7
def matrix_input():  # O(n^2)
    rows = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of col: "))
    list = []
    for i in range(rows):
        row = []
        for z in range(col):
            value = int(input(f"Enter the value at position ({i + 1},{z + 1}): "))
            row.append(value)
        list.append(row)
    return list
#
# part8
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return palindrome(s[1:-1])
    else:
        return False

# part9
def sequential_Search(s, list):  #O(n)
    for i in range(len(list)):
        if list[i] == s:
          print(f"{s} is found at index {i}")
          return i
    print(f"{s} is not found in the list")


# part10
def insertion_Sort(list):  # O(n^2)
    for x in range(len(list) - 1):
        for y in range(x + 1, len(list)):
            if list[x] > list[y]:
                temp = list[x]
                list[x] = list[y]
                list[y] = temp
    print(list)


def displayMenu():
    print("1. Add matrices\n"
          + "2. Check Rotation\n"
          + "3. Invert Dictionary\n"
          + "4. Convert Matrix to Dictionary\n"
          + "5. Check Palindrome\n"
          + "6. Search for an Element & Merge Sort\n"
          + "7. Exit")
def main():  #### Overall Time Complexity is O(n^2)
  displayMenu()
  choice = input("Enter your choice :")
  if choice == "1":  ## if user enter 1
       rows = int(input("Enter number of rows :"))
       col = int(input("Enter number of col :"))
       print("Enter elements of the first matrix")
       matrix1 = get_matrix(rows, col)  ## calling function for matrix 1
       print("Enter elements of the second matrix")
       matrix2 = get_matrix(rows, col)  ## calling function for matrix 2
       print("The sum of two matrices")
       result_matrix = add_Matrices(matrix1, matrix2)  ## adding matrix1 and matrix 2
       print(result_matrix)
       main()
  elif choice == "2":
        matrix1 = matrix_input()
        matrix2 = matrix_input()
        if rotation_matrix(matrix1, matrix2):
            print("Matrix 1 is a rotation of Matrix 2 .")
            print("The two matrices are rotations of each other.")
        else:
            print("Matrix 1 is not a rotation of Matrix 2.")
            print("The two matrices are not rotations of each other.")

        main()
  elif choice == "3":
        dictionary_input()
        main()
  elif choice == "4":
        rows = int(input("Enter rows :"))
        col = int(input("Enter col :"))
        convertMatrix_Dictionary(rows, col)
        main()
  elif choice == "5":
      word = input("Enter a word :")
      if palindrome(word):
          print(f"{word} is palindrome")
      else:
          print(f"{word} is not palindrome")
      main()
  elif choice == "6":
   list = [2, 4, 5, 12, 7, 1, 3]
   print(f"List : {list}")
   s = int(input("Enter an element to find :"))
   sequential_Search(s, list)
   print("list is sorted :")
   insertion_Sort(list)
   main()
  elif choice == "7":
      exit()
  else:
      print("invalid input please try again.")
      main()
if __name__ == '__main__':
    main()
