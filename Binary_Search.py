# BINARY SEARCH:

# def Binary_Search(arr,x):
#   n = len(arr)
#   low = 0
#   high = (n-1)

#   while low<=high:

#     mid = (low+high)//2

#     if arr[mid] == x:
#       return mid
      
#     elif arr[mid]<x:
#       low = mid+1
#     else:
#       high = mid-1

#   return -1

# print(Binary_Search([1,2,3,4,5,6],5))


#___________________________________________________________________________


# FIND LOWER BOUNND OF A GIVEN NUMBER:

# def LowerBound(arr,x):
#   n = len(arr)
#   low = 0
#   high = n-1
#   anss = n

#   while low<=high:

#     mid = (low+high)//2

#     if arr[mid]>=x:
#       anss = mid
#       high = mid-1
#     else:
#       low = mid+1
    
#   return anss

# print(LowerBound([1,2,3,3,7,8,9,9,9,11],10))


#___________________________________________________________________________


# FIND UPPER BOUNND OF A GIVEN NUMBER:

# def UpperBound(arr,x):
#   n = len(arr)
#   low = 0
#   high = n-1
#   anss = n

#   while low<=high:

#     mid = (low+high)//2

#     if arr[mid]<=x:
#       anss = mid
#       low = mid +1
#     else:
#       high = mid-1
    
#   return anss

# print(UpperBound([1,2,8,10,11,12,19],5))


#___________________________________________________________________________


# Find First and Last Position of Element in Sorted Array:

# def findOccur(nums,target):
#   def left(nums,target):
#     n = len(nums)
#     low = 0 
#     high = n-1
#     ans = n

#     while low<=high:
#       mid = (low+high)//2

#       if nums[mid]>=target:
#         ans = mid
#         high = mid -1
#       else:
#         low = mid+1
                
#     return ans
  

#   def right(nums,target):
#     n = len(nums)
#     low = 0 
#     high = n-1
#     ans = n

#     while low<=high:
#       mid = (low+high)//2

#       if nums[mid]<=target:
#         ans = mid
#         low = mid+1
#       else:
#         high = mid -1
           
#     return ans

#   left_ans = left(nums,target)
#   right_ans = right(nums,target)

#   if left_ans<=right_ans and nums[left_ans] == target:
#     return [left_ans,right_ans]
#   else:
#     return [-1,-1]
  
# print(findOccur([5,7,7,8,8,10],8))


#___________________________________________________________________________


# Count occurrences of a number in a sorted array with duplicates:

# def CountDup(nums,target):
#   def left(nums,target):
#     n = len(nums)
#     low = 0 
#     high = n-1
#     ans = n

#     while low<=high:
#       mid = (low+high)//2

#       if nums[mid]>=target:
#         ans = mid
#         high = mid -1
#       else:
#         low = mid+1
                
#     return ans
  

#   def right(nums,target):
#     n = len(nums)
#     low = 0 
#     high = n-1
#     ans = n

#     while low<=high:
#       mid = (low+high)//2

#       if nums[mid]<=target:
#         ans = mid
#         low = mid+1
#       else:
#         high = mid -1
           
#     return ans

#   left_ans = left(nums,target)
#   right_ans = right(nums,target)

#   if left_ans<=right_ans and nums[left_ans] == target:
#     return right_ans-left_ans+1
#   else:
#     return 0
  
# print(CountDup([5,7,7,10],5))


#___________________________________________________________________________


# SEARCH IN ROTATED SORT ARRAY WITHOUT DUPLICATES:

# def rotated(arr,x):
#   n = len(arr)
#   low = 0
#   high = n-1

#   while low<=high:

#     mid = (low+high)//2

#     if arr[mid] == x:
#       return mid

#     elif arr[mid] == arr[low] and arr[mid] == arr[high]:
#       high = high-1
#       low = low+1

#     elif arr[low]<=arr[mid]:
#       if arr[low]<=x and x<=arr[mid]:
#         high = mid-1
#       else:
#         low = mid+1

#     else:
#       if arr[mid]<=x and arr[high]>=x:
#         low = mid+1
#       else:
#         high = mid-1 

# print(rotated([1,0,1,1,1],0))


#___________________________________________________________________________


# Find Minimum in Rotated Sorted Array:

# def minni(nums):
#   n = len(nums)
#   low = 0
#   high = (n-1)
#   s = float('inf')

#   while low<=high:
#     mid = (low+high)//2

#     if nums[low]<=nums[mid]:
#       if s>nums[low]:
#         s = nums[low]
#       # s = min(s,nums[low])
#       low = mid + 1

#     else:
#       if s>nums[mid]:
#         s = nums[mid]
#       high = mid - 1
#       # if s>nums[mid]:
#       #   s = nums[mid]
#       # s = min(s,nums[mid])

#   return s

# print(minni([4,5,6,7,0,1,2]))


#___________________________________________________________________________


# FIND HOW MUCH TIME ARRAY HAS BEEN ROTATED:

# def minni(nums):
#   n = len(nums)
#   low = 0
#   high = (n-1)
#   s = float('inf')
#   posi = 0

#   while low<=high:
#     mid = (low+high)//2

#     if nums[low]<=nums[mid]:
#       if s>nums[low]:
#         s = nums[low]
#         posi = low
#       low = mid + 1

#     else:
#       if s>nums[mid]:
#         s = nums[mid]
#         posi = mid
#       high = mid - 1

#   return posi

# print(minni([1,0]))


#___________________________________________________________________________

# FIND PEAK ELEMENT:

# def find(arr):
#   low = 0
#   high = len(arr)

#   while low<=high:

#     mid = (low+high)//2

#     if (mid == 0 or arr[mid]>=arr[mid-1]) and (mid == len(arr)-1 or arr[mid]>=arr[mid+1]):
#       return mid
#     elif arr[mid-1]>=arr[mid]:
#       high = mid-1
#     else:
#       low = mid+1

# print(find([1,2]))


#___________________________________________________________________________


# FIND SQUARE ROOT OF A NUMBER OR RETURN ITS FLOOR VALUE:

# def find_sq(num):
#   low = 1
#   high = num//2
#   ans = 0

#   if num == 1:
#     return 1

#   while low<=high:
#     mid = (low+high)//2

#     if mid*mid <= num:
#       ans = mid
#       low = mid+1

#     else:
#       high = mid-1

#   return ans

# print(find_sq(5))


#___________________________________________________________________________


# SINGLE ELEMENT IN A SORTED ARRAY:

# def find_single(nums):
#     n = len(nums)
#     low = 0
#     high = n-1

#     if n == 1:
#         return nums[0]

#     else:
#         while low<=high:
#             mid = (low+high)//2

#             if (mid == 0 or nums[mid]!=nums[mid-1]) and (mid == n-1 or nums[mid]!=nums[mid+1]):
#                 return nums[mid]

#             elif (mid%2 == 1 and nums[mid] == nums[mid-1]) or (mid%2 == 0 and nums[mid] == nums[mid+1]):
#                 low = mid+1
#             else:
#                 high = mid-1


#___________________________________________________________________________


# KOKO EATING BANANAS:

# from math import ceil
# def koko_Eat_banana(arr,h):
#   n = len(arr)
#   maxi = max(arr)
#   low = 1
#   high = maxi

#   while low<=high:
#     mid = (low+high)//2
#     hrs = 0

#     for j in range(n):
#       a = arr[j]/mid
#       a = ceil(a)
#       hrs+=a

#     if hrs<=h:
#       high = mid-1

#     else:
#       low = mid+1

#   return low

# print(koko_Eat_banana([3,6,7,11],8))


#___________________________________________________________________________


# MINIMUM NUMBER OF DAYS TO MAKE M BOUQUETS:

# def minDays(arr,m,k):
#   n = len(arr)
#   low = 1
#   high = max(arr)
#   res = -1

#   while low<=high:
#     mid = (low+high)//2
#     c = 0
#     l = 0
            
#     for s in range(n):
#       if arr[s]<=mid:
#         c+=1

#         if c == k:
#           l+=1
#           c = 0

#       else:
#         c = 0

#     if l<m:
#       low = mid+1
#     else:
#       res = mid
#       high = mid-1

#   return res


#___________________________________________________________________________


# CAPACITY TO SHIP PACKAGES WITHIN D DAYS:

# def shipWithinDays(arr,days):
#   n = len(arr)
#   low = max(arr)
#   high = sum(arr)

#   while low<=high:
#     mid = (low+high)//2
#     summ = 0
#     c = 1

#     for i in range(n):
#       summ+=arr[i]

#       if summ>mid:
#         c+=1
#         summ = arr[i]

#     if c<=days:
#       high = mid-1

#     else:
#       low = mid+1

#   return low


#___________________________________________________________________________


# AGGRESIVE COW:

# def canPlace(arr,i,cow):
#   c = 1
#   a = arr[0]

#   for j in range(1,len(arr)):

#     if arr[j] - a >= i:
#       a = arr[j]
#       c+=1

#     if c>=cow:
#       return True
    
#   return False

# def cow(arr,cow):
#   arr1 = sorted(arr)
#   n = len(arr1)
#   low = 1
#   high = max(arr1)-min(arr1)

#   while low<=high:

#     mid = (low+high)//2

#     if canPlace(arr1,mid,cow) == True:
#       low = mid+1

#     else:
#       high = mid-1

#   return high

# print(cow([1,2,8,4,9],3))


#___________________________________________________________________________


# ALLOCATE BOOKS:

# def chechBook(arr,pages):
#   n = len(arr)
#   stu = 1
#   p = 0
#   for j in range(n):

#       if p+arr[j] <= pages:
#         p += arr[j]

#       else:
#         stu += 1
#         p = arr[j]
        
#   return stu

# def allocate_book(arr,m,n):
#   low = max(arr)
#   high = sum(arr)

#   while low<=high:

#     mid = (low+high) // 2

#     stunum = chechBook(arr,mid) 

#     if stunum > m:
#       low = mid + 1

#     else:
#       high = mid - 1

#   return low


#___________________________________________________________________________


# SPLIT ARRAY LARGEST SUM:

# def checkSum(arr,summ):
#   posi = 1
#   sum1 = 0

#   for i in range(len(arr)):

#     if sum1 + arr[i] <= summ:
#       sum1 += arr[i]

#     else:
#        posi+=1
#        sum1 = arr[i]

#   return posi

# def splitarr(arr,k):
#   low = max(arr)
#   high = sum(arr)

#   while low<=high:

#     mid = (low+high) // 2

#     ans = checkSum(arr,mid)

#     if ans > k:
#       low = mid+1

#     else:
#       high = mid-1

#   return low

# print(splitarr([7,2,5,10,8],2))


#___________________________________________________________________________


# Painter's Partition Problem:

# def check(arr,summ):
#   n = len(arr)
#   board = 0
#   p = 1

#   for i in range(n):
#     board+=arr[i]

#     if board > summ:
#       board = arr[i]
#       p+=1

#   return p

# def PainterPartition(arr,k):
  
#   low = max(arr)
#   high = sum(arr)

#   while low<=high:

#     mid = (low+high)//2

#     ans = check(arr,mid)

#     if ans>k:
#       low = mid+1

#     else:
#       high = mid-1

#   return low

# print(PainterPartition([2, 1, 5, 6, 2, 3],2))


#___________________________________________________________________________

# MEDIAN OF TWO SORTED ARRAY:

def median(arr1,arr2):
  arr = sorted(arr1+arr2)
  # arr3 = sorted(arr)
  n = len(arr)
  low = 0
  high = n-1

  mid = (low+high)//2

  if n%2!=0:
    ans = arr[mid]

  else:
    ans = (arr[mid]+arr3[mid+1])/2

  return ans

print(median([1,3],[2]))