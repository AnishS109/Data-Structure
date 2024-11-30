# def merge(arr,left,right):
#   i = j = k = 0

#   while i<len(left)  and j<len(right):
#     if left[i]<right[j]:
#       arr[k] = left[i]
#       i+=1
#     else:
#       arr[k] = right[j]
#       j+=1
#     k += 1

#   while i<len(left):
#     arr[k] = left[i]
#     i+=1
#     k+=1

#   while j<len(right):
#     arr[k] = right[j]
#     j+=1
#     k+=1

#   return arr

# def merge_sort(arr):
  
#   if len(arr)>1:
#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:] 

#     merge_sort (left)
#     merge_sort (right)
#     return merge(arr,left,right)
  
#   else:
#     return arr

# print(merge_sort([1,2,3,4,5]))


#___________________________________________________________________________


# MERGE SORT IN DESCENDING ORDER:

# def merge(arr,left,right):

#   i = j = k = 0

#   while i<len(left) and j<len(right):
#     if left[i]>right[j]:
#       arr[k] = left[i]
#       i+=1
#     else:
#       arr[k] = right[j]
#       j+=1
    
#     k+=1
  
#   while i<len(left):
#     arr[k] = left[i]
#     i+=1
#     k+=1

#   while j<len(right):
#     arr[k] = right[j]
#     j+=1
#     k+=1

#   return arr

# def merge_sort(arr):

#   if len(arr)>1:

#     mid = len(arr)//2
#     left = arr[:mid]
#     right = arr[mid:]

#     merge_sort(left)
#     merge_sort(right)

#     return merge(arr,left,right)
  
#   else:
#     return arr
  
# print(merge_sort([1,2,3,4,5,6]))