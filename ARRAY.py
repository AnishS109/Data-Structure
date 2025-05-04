# find largest element in array:

# def find(nums):
#    l = nums[0]
#    for i in range(1,len(nums)):
#      if nums[i]>l:
#         l = nums[i]
#    print(l)

# find([10,3,5,7,8,4,5])


# ______________________________________________________________________________________________________


# find second largest element in array:

# def secondLarge(arr):

#   n = len(arr)
#   large = arr[0]
#   Slarge = -3

#   for i in range(n):
#     if arr[i]>large:
#       large = arr[i]

#     if arr[i]>Slarge and arr[i]!=large:
#       Slarge = arr[i]

#   return Slarge

# print(secondLarge([-1,-2,-3,-4,-5]))


# ______________________________________________________________________________________________________


# find smalest number in array:

# def find_Smallest(nums):
#    S = nums[0]
#    n = len(nums)

#    for i in range(1,n):
#       if nums[i]<S:
#          S = nums[i]
#    print(S)

# find_Smallest([5,7,4,3,6,8,4,2,2])


# ______________________________________________________________________________________________________


# Check if the array is sorted or not:

# def find_is_sorted(nums):
  
#   n = len(nums)

#   for i in range(1,n):
#     if nums[i]>=nums[i-1]:
#       pass
#     else:
#       return False
#   return True

# print(find_is_sorted([1,2,3,4,5]))


# ______________________________________________________________________________________________________


# Remove duplicate from sorted array:

# def remove_duplicate(nums):
#   n = len(nums)
#   s = []

#   for i in range(0,n):
#     if nums[i]!=nums[i-1]:
#       s.append(nums[i])
#   print(s)

# remove_duplicate([1,1,1,2,2,3,4,5])


# ______________________________________________________________________________________________________


# Rotate the array from one place:

# def rotate_one(nums):
  
#   n = len(nums)
#   a = nums[0]

#   for i in range(1,n):
#     nums[i-1] = nums[i]
#   nums[n-1] = a
#   print(nums)

# rotate_one([1,2,3,4,5])


#___________________________________________________________________________


# Rotate and array with k element:

# def rotate(nums,b):
#   n = len(nums)
#   temp = [None] * n

#   for i in range(n):
#     temp[(i+b)%n] = nums[i]    

#   print(temp)

# rotate([1,2,3,4,5,6,7],8)


#___________________________________________________________________________


# Move all 0 to the left side of the array:

# def rotate(nums):
#   n = len(nums)
#   temp = []

#   for i in range(n):
#     if nums[i]!=0:
#       temp.append(nums[i])

#   for i in range(len(temp)):
#     nums[i] = temp[i]

#   for i in range(len(temp),n):
#     nums[i] = 0
#   print(nums)

# rotate([1,2,3,0,4,0,5,0,6,7,8])


#___________________________________________________________________________


# Linear Search:

# def linear(nums,b):
#   n = len(nums)

#   for i in range(n):
#     if nums[i] == b:
#       print(i)
    
# linear([1,2,34,3,2,1,3,5,4],4)


#___________________________________________________________________________


# Union of two sorted array:

# def unegon(nums,arr2):
#   n = len(nums)
#   N =len(arr2)
#   unegon = []
#   U = len(unegon)
#   i = 0
#   j = 0

#   while i<n and j<N:
#     if nums[i]<arr2[j]:
#       if U == 0 or unegon[-1] != nums[i]:
#         unegon.append(nums[i])
#         i += 1
#     elif nums[i]>arr2[j]:
#       if U == 0 or unegon[-1] != arr2[j]:
#         unegon.append(arr2[j])
#         j += 1
#     else:
#       if U == 0 or unegon[-1] != nums[i]:
#         unegon.append(nums[i])
#         i += 1
#         j += 1

#   while i < n:
#     if U == 0 or unegon[-1] != nums[i]:
#         unegon.append(nums[i])
#         i += 1
    
#   while j < N:
#     if U == 0 or unegon[-1] != arr2[j]:
#         unegon.append(arr2[j])
#         j += 1
  
#   print(unegon)

# unegon([1,2,3,4],[5,6,7,8])


#___________________________________________________________________________


# Intersection of two arrays

# def inter(a1,a2):
#   N =len(a2)
#   n = len(a1)
#   temp = []
#   U = len(temp)
#   i = 0
#   j = 0

#   for i in range(0,n):
#     for  j in range(0,N):
#       if (a1[i] == a2[j]) and (U == 0 or temp[-1] != a1[i]):
#         temp.append(a1[i])
#         j = j+1
#         break
      
#       else:
#         j = j+1

#   print(temp)

# inter([1,2,3,4,5],[3,3,3,3,3,3,4,5])


#___________________________________________________________________________


# Find missing number

# def find(nums):
#   n = len(nums)

#   for i in range(1,n+1):
#     for j in range(n):
#       if i
#       i == nums[j]:
#         break
#       else:
#         ()
      
#   return i

# print(find([1,2,3,4,5,7]))


#___________________________________________________________________________


# Print number that appear once

# def find_once(nums):
#   n = len(nums)
#   b = 0

#   for i in range(n):
#     for j in range(i+1,n):

#       if nums[i] != nums[j] or nums[i] != nums[i-1]:
#         continue
#       else:
#         break

#     return nums[i]

# print(find_once([1,1,2,3,3]))


#___________________________________________________________________________


# Largest subarray wiht sum K

# def subarray(nums,k):
#   n = len(nums)
#   res = []

#   for i in range(n):
#     sum = 0
#     for j in range(i,n):
#       sum = sum+nums[j]

#       if sum == k:
#         res.append(nums[i:j+1])
#     break
      

#   return res

# print(subarray([1,2,1,2,3,4],6))


#___________________________________________________________________________


# Major element

# def sub(nums):
#   n = len(nums)      
#   for i in range(n):
#     count = 1
#     for j in range(i+1,n):
#       if nums[i] == nums[j]:
#         count = count+1
#         if count>(n/2):
#           return nums[i]
        
# print(sub([1,2,2,3,4,4,4,4,4,4]))


#___________________________________________________________________________


# arrange consecutive opposite sign elements in array

# def find(nums):
#   n = len(nums)
#   pos = 0
#   neg = 1
#   res = [0] * len(nums)
        
#   for n in nums:
#     if n > 0:
#       res[pos] = n
#       pos += 2
#     else:
#       res[neg] = n
#       neg += 2
        
#   return res
      
# print(find([3,2,1,-1,-2,-3,-2,-1,6,5]))


#___________________________________________________________________________


# Best time to buy and sell stock

# def find(prices):
#   n = len(prices)
#   s = prices[0]
  
#   if n > 1:
#     for i in range(1,n):
#       if prices[i]<s:
#         s = prices[i]
  
#     a = prices.index(s)
#     l = prices[a]

#     for i in range(a,n):
#       if prices[i]>l:
#         l = prices[i]
    
#     return l-s
  
#   else:
#     return 0

# print(find([2,4,1]))


#___________________________________________________________________________


# FIND LEADERS IN GIVEN ARRAY:

# def find_leader(arr):
#   n = len(arr)
#   a = []
#   mx = float()

#   for i in range(n-1,-1,-1):
#     if i>mx:
#       mx = i 
#       a.append(mx)

#   # for i in range(n):
#   #   leader = True
#   #   for j in range(i+1,n):
#   #     if i<arr[j]:
#   #       leader = False
#   #       break

#   #   if leader == True:
#   #     a.append(i)

#   return a

# print(find_leader([10,22,12,13,0,6]))


#___________________________________________________________________________


# MAXIMUM PRODUCT SUBARRAY:

# def max_product(arr):
#   n = len(arr)
#   mx = float()
#   a = []

#   for i in range(n):
#     pro = 1
#     for j in range(i,n):
#       pro = pro*arr[j]
#       a.append(pro)
      
#   return max(a)
     
# print(max_product([2,3,4,5]))


#___________________________________________________________________________


# MAJORITY ELEMENT:

# def find_majority(arr):
#   n = len(arr)
#   a = []
#   c = (n//3)
  
#   for i in range(n):
#     count = 0
#     for j in range(i,n):
#       if i==arr[j]:
#         count += 1
#         if count > c:
#          a.append(i)
#   return a
  
# print(find_majority([1,1,1,2,2,2,4,4]))


#___________________________________________________________________________


# 3 SUM PROBLEM:

# def three_sum(arr,k):
#   arr.sort()
#   n = len(arr)
#   a = set()

#   for i in range(n):
#     for j in range(i+1,n):
#       for p in range(j+1,n):
#         if (i+arr[j]+arr[p]) == k:
#           a.add((i,arr[j],arr[p]))   

#   return a

# print(three_sum([-1,-1,0,1,2],0))


#___________________________________________________________________________


# INSERT GIVEN ELEMENT ON GIVEN INDEX:

# def insert(arr,N,ni):
#   n =len(arr)
#   arr1 = []

#   for i in range(n):
#     if i == ni:
#       arr1.append(N) 

#     arr1.append(arr[i]) 
    
#   return arr1

# print(insert([1,2,3,5],44,3))


#___________________________________________________________________________


# REMOVE DUPLICATES (atmost 2 times at one element) AND RETURN LENGHT OF ARRAY:

# def removeDup(arr):
#   n = len(arr)

#   if n<=2:
#     return n
  
#   k = 2

#   for i in range(2,n):
#     if arr[i] != arr[k-2]:
#       arr[k] = arr[i]
#       k+=1

#   return k

# print(removeDup([1,1,1,2,2,2,3]))


#___________________________________________________________________________


# Contiguous Array:

# def conti(arr):
#   n = len(arr)
#   arr1 = []

#   for i in range(n):
#       count_1 = 0
#       count_0 = 0

#       for j in range(i,n):

#         if arr[j] == 1:
#           count_1 +=1
#         else:
#           count_0 +=1

#         if count_1 == count_0:
#           arr1.append(arr[i:j+1])
      
#   return max(len(s) for s in arr1)

# print(conti([1,0,1,1,1,0,0,0]))


#___________________________________________________________________________


# MAXIMUM NUMBER OF INTEGERS TO CHOOSE FROM A RANGE I:

# def maxCount(banned,a,maxSum):
#   banned_set = set(banned)
#   count = 0
#   Sum = 0

#   for i in range(1,a+1):

#     if i not in banned_set and Sum + i <= maxSum:
#       Sum += i
#       count += 1

#   return count

# print(maxCount([1,5,6],5,6))


#___________________________________________________________________________


# NEXT PERMUTAION:

# def next(arr):
#   n = len(arr)
#   indexx = -1

#   for i in range(n-2,-1,-1):
#     if arr[i]<arr[i+1]:
#       indexx = i
#       break

#   if indexx == -1:
#     arr.reverse()
#     return arr

#   for i in range(n-1,indexx,-1):
#     if arr[i]>arr[indexx]:
#       arr[i],arr[indexx] = arr[indexx],arr[i]
#       break

#   arr[indexx + 1:] = reversed(arr[indexx + 1:])
#   return arr

# print(next([1,2,3,4,5]))


#___________________________________________________________________________


# REARRANGE ARRAY ELEMENTS BY SIGN:

# def reArrange(arr):
#   n = len(arr)
#   a = [0] * n
#   posi = 0
#   negi = 1

#   for i in arr:

#     if i>0:
#       a[posi] = i
#       posi+=2

#     else:
#       a[negi] = i
#       negi+=2

#   return a

# print(reArrange([1,2,3,-1,-2,-3]))


#___________________________________________________________________________


# FIND SUB_ARRAY WITH LARGEST SUM:

# def maxSubArray(arr):
#   n = len(arr)
#   maxSum = float('-inf')
#   Sum = 0

#   if (n == 1):
#     return arr[0]
  
#   for i in range(n):
#     Sum += arr[i]

#     if Sum>maxSum:
#       maxSum = Sum

#     if Sum<0:
#       Sum = 0

#   return maxSum

# print(maxSubArray([5,4,-1,7,8]))


# ________________________________________________________________________


# SORT COLORS

def sortColors(nums):
  n = len(nums)
  arr = []
  zero = 0
  one = 0
  two = 0

  for i in nums:
      if i == 0:
          zero += 1
      elif i == 1:
          one += 1
      else:
          two += 1

  for i in range(n):
      if zero>0:
          arr.append(0)
          zero -= 1
      elif one>0:
          arr.append(1)
          one -= 1
      else:
          arr.append(2)
          two -= 1
  
  return arr

# ------------------------------- LONGEST COMMONN PREFIX ------------------------------

def longestCommonPrefix(strs):
    strs.sort()
    print(strs)
    str1 = strs[0]
    str2 = strs[len(strs) - 1]
    n = len(str1)
    ans = ""

    for i in range(n):
        if str1[i] == str2[i]:
            ans = ans + str1[i]
    return ans

print(longestCommonPrefix(["dog","racecar","car"]))