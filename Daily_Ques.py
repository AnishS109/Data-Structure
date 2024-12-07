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


