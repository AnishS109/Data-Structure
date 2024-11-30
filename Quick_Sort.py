# BRUTE APPROACH:

# def quick_sort(arr):

#   if len(arr)<=1:
#     return arr
  
#   else:
#     pivot = arr[(len(arr))//2]
#     left = [x for x in arr if x<pivot]
#     right = [y for y in arr if y>pivot]
#     mid = [z for z in arr if z==pivot]
#     return quick_sort(left) + mid + quick_sort(right)
  
# print(quick_sort([10,8,6,4,2,1,3,5,7,9]))


#___________________________________________________________________________


# OPTIMIZED APPROACH:

# def partiton(arr,low,high):

#   pivot = arr[high]
#   i = low-1
#   for j in range(low,high):
#     if arr[j]<=pivot:
#       i+=1
#       arr[i],arr[j] = arr[j],arr[i]

#   arr[i+1],arr[high] = arr[high],arr[i+1]
#   return i+1

# def quick_sort(arr,low,high):

#   if low<high and len(arr)>1:
#     pi = partiton(arr,low,high)
#     quick_sort(arr,low,pi-1)
#     quick_sort(arr,pi+1,high)
#     return arr
  
#   else:
#     return arr

# print(quick_sort([1,2,3,10,9,8,7,6,5,4],3,9))


#___________________________________________________________________________


# Quick SORT IN DESCENDING ORDER:

def partition(arr,low,high):

  pivot = arr[high]
  i = low-1

  for j in range(low,high):
    if arr[j]>=pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]

  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1

def quick_sort(arr,low,high):

  if low<high and len(arr)>1:

    pi = partition (arr,low,high)
    quick_sort(arr,low,pi-1)
    quick_sort(arr,pi+1,high)
    return arr
  
  else:
    return arr
  
print(quick_sort([5,4,3,2,1,7,8,9,6],0,8))