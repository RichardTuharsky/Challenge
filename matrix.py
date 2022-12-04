from random import randint

def initialiseMatrix(matrix,n):
  for row in range(0,n):
    matrix.append([])
    for col in range(0,n):
      value = randint(0,99)
      matrix[row].append(value)
  
def displayMatrix(matrix):
  n = len(matrix)
  for row in range(0,n):
    st="| " 
    for col in range(0,n):
      if matrix[row][col]<10:
        st = st + str(matrix[row][col]) + "  | "
      else:
        st = st + str(matrix[row][col]) + " | "
    print(st)

def calculateMatrix(matrix):
    n = len(matrix) #row
    m = len(matrix[0]) #col
    
    corner_sum = (matrix[0][0] + matrix[0][m - 1] + matrix[n - 1][0] + matrix[m - 1][n - 1])
    
    print(corner_sum)
    
def calculateAverageValue(matrix):
    n = len(matrix)
    for row in range(0, n):
        for col in range(0, n):
            sum = matrix[row][col] / n * n
            
            
    print(sum)
            

n = int(input("Enter the dimension n of your square matrix. (e.g. 3): "))

matrix = []
initialiseMatrix(matrix,n)
displayMatrix(matrix)
calculateMatrix(matrix)
calculateAverageValue(matrix)
    
  
