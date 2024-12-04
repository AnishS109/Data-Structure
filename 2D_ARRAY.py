# Linear Seaarch in 2D ARRAY

# def find(arr,x):
   
#   n = len(arr)
#   m = len(arr[0])

#   for i in range(n):
#     for j in range(m):
#       if arr[i][j] == x:
#         print("Yes")

# find([[1,2,3],[4,5,6],[7,8,9]],9)


#___________________________________________________________________________________________________


# ROW WISE SUM:

# def row_sum(arr):

#   n = len(arr)
#   m = len(arr[0])
#   l = []

#   for i in range(n):
#     sum = 0
#     for j in range(m):
#       sum += arr[i][j]
#     print(sum)

# row_sum([[1,2,3],[4,5,6]])


#___________________________________________________________________________________________________


# LARGEST SUM OF ROWS:

# def row_sum(arr):
#   n = len(arr)
#   m = len(arr[0])
#   mx = float()

#   for i in range(n):
#     sum = 0
#     for j in range(m):
#       sum += arr[i][j]
#     if sum>mx:
#       mx = sum
  
#   print(mx)
# row_sum([[1,2,3],[4,5,6],[7,8,9],[1,3,5]])


#___________________________________________________________________________________________________


# PRINT WAVE WISE

# def printt_wave(arr):
#   n = len(arr)
#   m = len(arr[0])
#   turn = 0

#   for j in range(m):

#     if turn%2 == 0:
#       for i in range(n):
#         print(arr[i][j])
    
#     else:
#       for i in range(n-1,-1,-1):
#         print(arr[i][j])

#     turn += 1

# printt_wave([[1,2,3],[4,5,6],[7,8,9]])


#___________________________________________________________________________________________________


# SPIRAL PRINT

# def spiral(arr):

#   n = len(arr)
#   m = len(arr[0])

#   top = 0
#   bottom = (n-1)
#   left = 0
#   right = (m-1)

#   while top<=bottom and left<=right:
#     for i in range(left,right+1):
#       print(arr[top][i])
#     top += 1

#     for i in range(top,bottom+1):
#       print(arr[i][right])
#     right -= 1

#     for i in range(right,left-1,-1):
#       print(arr[bottom][i])
#     bottom -= 1

#     for i in range(bottom,top-1,-1):
#       print(arr[i][left])
#     left += 1

# spiral([[1,2,3,4,5],[16,17,18,19,6],[15,24,25,20,7],[14,23,22,21,8],[13,12,11,10,9]])  


#___________________________________________________________________________________________________


# CONVERT 1D ARRAY INTO 2D ARRAY

# def construct2DArray(original,m,n):
#         if m * n != len(original):
#           return []
        
#         res = []
#         for i in range(0, len(original),n):
#             res.append(original[i : i+n])
        
#         return res

# print(construct2DArray([1,2,3,4],2,2))
 

#___________________________________________________________________________________________________


# SEARCH IN 2D ARRAY:

# def searchMatrix(matrix,target):
#         n = len(matrix)
#         m = len(matrix[0])
#         a = None
        
#         for i in range(n):
#                 for j in range(m):
#                         if target == matrix[i][j]:
#                                 a = target
#         if a != None:
#                 return True
#         else:
#                 return False
                          
# print(searchMatrix([[1,2,3],[4,5,6]],7))


#___________________________________________________________________________________________________


# SET MATRIX ZEROS:

# def row(arr,i):
#   m = len(arr[0])
#   for j in range(m):
#     if arr[i][j] != 0:
#       arr[i][j] = -1

# def col(arr,j):
#   n = len(arr)
#   for i in range(n):
#     if arr[i][j] != 0:
#       arr[i][j] = -1

# def set_matrix(arr):
#   n =  len(arr)
#   m = len(arr[0])

#   for i in range(n):
#     for j in range(m):
#       if arr[i][j] == 0:
        
#         row(arr,i)
#         col(arr,j)

#   print(arr)

# set_matrix([[1,1,1,1,1],[1,1,1,1,1],[1,1,0,0,1],[1,1,1,0,1],[1,1,1,1,1]])


#___________________________________________________________________________________________________


# ROW WITH MAX 1s:

# def row(arr):
#   n = len(arr)
#   m = len(arr[0])
#   a = []

#   for i in range(n):
#     low = 0
#     high = m-1
#     count = 0
              
#     while low<=high:
#       mid = (low+high) // 2
                   
#       if arr[i][mid] == 1:
#         high = mid-1
#       else:
#         low = mid+1

#     count = m-low
#     a.append(count)

#   return a.index(max(a))

# print(row([[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]))