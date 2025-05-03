# TOPIC - BINARY SEARCH:

# QUESTION ----- MINIMUM LIMIT OF BALLS IN A BAG:

# import math
# def isPossible(nums,x,maxOps):
#   n = len(nums)
#   ops = 0

#   for i in range(n):
#     if nums[i] > x:

#       bags = math.ceil(nums[i]/x)
#       ops+=bags-1

#     if ops>maxOps:
#       return False
  
#   return True

# def minimumSize(nums,maxOps):
#   n = len(nums)

#   low = 1
#   high = max(nums)
#   res = 0

#   while low<=high:

#     mid = (low+high)//2

#     a = isPossible(nums,mid,maxOps)

#     if a == True:
#       res = mid
#       high = mid-1

#     else:
#       low = mid+1

#   return res

# print(minimumSize([9],2))


# ______________________________________________________________________________


# TOPIC - BINARY SEARCH:

# a = [[1,3,2],[4,5,2],[2,4,3]]
# print(sorted(a))

# print(max(a[0]))

# def check(arr,x):
#   n = len(arr)
#   m = len(arr[0])
#   S = arr[0][0]
#   E = arr[0][1]
#   sum = arr[0][2]

#   for i in range(2,n):
#     for j in range(2,m):

#       if j == 0:
#         if S<=arr[i][j]<=E:
#           break
#         S = arr[i][j]
      
#       if j == 2:
#         sum+=arr[i][j]

#       if sum > x:
#         return False

#   return True

# def maxi(arr):
#   low = 1
#   high = 0
#   res = 0
#   for i in range(len(arr)):
#     high += arr[i][2]

#   while low <= high:
#     mid = (low+high)//2

#     a = check(arr,mid)

#     if a == True:
#       res = mid
#       low = mid+1
#     else:
#       high = mid-1

#   return res 

# print(maxi([[1,3,2],[4,5,2],[1,5,5]]))
# import math
# a = math.ceil(2/3)
# b = 1//3
# print(b)

def majo(arr):
  n = len(arr)
  res = []
  final = []
  m = n//3
  print(m)

  for i in range(n):

    if arr[i] not in res:
      res.append(arr[i])
      res.append(1)

    else:
      a = res.index(arr[i])
      b = a+1
      res[b]+=1

  c = len(res)

  for i in range(1,c-1,2):
    if arr[i]>m:
      final.append(arr[i-1])
  
  return final
print(majo([2,2]))