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

