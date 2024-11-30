# def cycle_sort(arr):
  
#   n = len(arr)

#   for i in range(n-1):
#     item = arr[i]
#     Pos = i

#     for j in range(i+1,n):
#       if arr[j]<item:
#         Pos+=1

#     if Pos == i:
#       continue

#     while item == arr[Pos]:
#       Pos+=1

#     arr[Pos],item = item,arr[Pos]

#     while Pos!= i:
#       Pos = i

#       for j in range(i+1,n):
#         if arr[j]<item:
#           Pos+=1

#       while item == arr[Pos]:
#         Pos+=1
#       arr[Pos],item = item,arr[Pos]

#   return arr

# print(cycle_sort([5,4,3,2,1,5,5,67,4,34,5,6,6,7,8,9,8,7,6,6,5,4,3,232,34,5,65,67]))


#___________________________________________________________________________


# SET MIS_MATCH:

# def setMis(arr):
#   n = len(arr)
#   miss = None
#   seen = set()
#   dup = None

#   for i in range (n):
    
#     if arr[i] in seen:
#       dup = arr[i]
#     else:
#       seen.add(arr[i])

#   for i in range(1,n+1):
#     if i not in seen:
#       miss = i
#       break

#   return [dup,miss]

# print(setMis([1,1]))
  