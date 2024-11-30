# BUBBLE SORT:

# def bubble(str):
#   n = len(str)

#   for i in range(n-1):
    
#     for j in range(n-i-1):
#       if (str[j]>str[j+1]):
#         str[j],str[j+1] = str[j+1],str[j]

#   print(str)

# bubble([12,9,4,1,13,2,3,14,8,7,6,5,10,11])


#___________________________________________________________________________


# ENHANCED VERSION OF BUBBLE SORT:

# def bubble(str):
#   n = len(str)

#   for i in range(n-1):
#     is_sorted = True
#     for j in range(n-i-1):
#       if (str[j]>str[j+1]):
#         is_sorted = False
#         str[j],str[j+1] = str[j+1],str[j]

#     if is_sorted == True:
#       break

#   print(str)


#___________________________________________________________________________


# MAXIMUM SWAPS ARE NEEDED TO SORT strAY OF LENGTH 6:

# def bubble(str):
#   n = len(str)
#   count = 0

#   for i in range(n-1):
    
#     for j in range(n-i-1):
#       if (str[j]>str[j+1]):
#         str[j],str[j+1] = str[j+1],str[j]
#         count += 1

#   print(str,count)

# bubble([6,5,4,3,2,1])


#___________________________________________________________________________


# SORT STRING IN DECREASING ORDER AFTER REMOVAL OF VALUES SMALLER THEN K:

# def sort_string(str,k):
#   str1 = str.split()
#   n = len(str1)
#   str2 = []

#   for i in range(1,n,2):
#     if int(str1[i])>k:
#       str2.append(str1[i-1])
#       str2.append(str1[i])

#   n2 = len(str2)

#   for i in range(1,n2,2):
#     for j in range(1,n2-i,2):
#       if str2[j]<str2[j+2]:
#         str2[j],str2[j+2] = str2[j+2],str2[j]
#         str2[j-1],str2[j+1] = str2[j+1],str2[j-1]

#   return " ".join(str2)

# print(sort_string("anish 90 Yash 91 Saini 92 kunnu 80 yash 50",75))


#___________________________________________________________________________


# PUSH ZEROES TO END:

# def push_zero(arr):
#   n = len(arr)

#   for i in range(n):
#     for j in range(n-i):
#       if j+1<n:
#         if arr[j] == 0:
#           arr[j],arr[j+1] = arr[j+1],arr[j]

#   return arr

# print(push_zero([1,2,0,4,3,0,5,0]))