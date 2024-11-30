# a = [1,2,3,4]
# def printnum(a,i):
#     if i>=len(a):
#         return
#     else:
#         print(a[i])
#     printnum(a,i+1)
# printnum(a,0)


#___________________________________________________________________________



# a = [1,2,3,4]
# def revNum(a,i):
#     if i>=len(a):
#         return
#     revNum(a,i+1)
#     print(a[i])
# revNum(a,0)


#___________________________________________________________________________



# def fact(a):
#     if  a == 0:
#         return 1
#     else:
#         return a*fact(a-1)
# print(fact(4))


#___________________________________________________________________________



# def fibo(n):
#     if n <=1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
# print(fibo(6))      


#___________________________________________________________________________



# def sumArr(a):
#     if len(a) == 0:
#         return 0
#     else:
#         return a[0]+sumArr(a[1:])
# print(sumArr([1,2,3,4]))


#___________________________________________________________________________



# def revStr(a,i):
#     if i>=len(a):
#         return 0
#     else:
#         revStr(a,i+1)
#         print(a[i])
# print(revStr("Anish",0))


#___________________________________________________________________________



# def pow(a,b):
#     if a and b == 1:
#         return 1
#     else:
#         return a**b
# print(pow(5,2))


#___________________________________________________________________________



# def revStr(n,i):
#     if i>=len(n):
#         return 0
#     else:
#         revStr(n,i+1)
#         print(n[i])
# revStr("ANish",0)


#___________________________________________________________________________


# def printNum(n):
#     if n<=0:
#         return 0
#     else:
#         printNum(n-1)
#         print(n)
# printNum(5)


#___________________________________________________________________________


# Stair Step Problem

# def step_stair(n):
#     if n<=1:
#         return 1
#     elif n<<0:
#         return 0
#     else:
#         return step_stair(n-1)+step_stair(n-2)
# print(step_stair(3))


#___________________________________________________________________________
#___________________________________________________________________________
#___________________________________________________________________________
#___________________________________________________________________________
#___________________________________________________________________________


# PRINT NUMBER WITH GIVEN RANGE:

# def repeat(i,a):
#   if i>a:
#     return
#   else:
#     print(i)
#     repeat(i+1,a)

# repeat(1,25)


#___________________________________________________________________________


# PRINT STRING FROM USER INPUT TIMES:

# def linear(a,n):

#   if a>n:
#     return
#   else:
#     print("Meko Recursion ata h")
#     linear(a+1,n)

# linear(4,4)


#___________________________________________________________________________


# PRINT REVERSE NUMBER USING BACK_TRACKING:

# def revNum(i):

#   if i<=0:
#     return
#   else:
#     revNum(i-1)
#     print(i)

# revNum(10)


#___________________________________________________________________________


# PRINT SUM OF N NUMBERS:

# def sumNum(i,sum):
#   if i<0:
#     print(sum)
#     return
#   sumNum(i-1,sum+i)

# sumNum(4,0)


#___________________________________________________________________________


# PRINT SUM OF N NUMBERS OPTIMIZED APPROACH:

# def sumNUM(n):

#   if n == 0:
#     return 0
#   return n + sumNUM(n-1)

# print(sumNUM(5))


#___________________________________________________________________________


# REVERSE AN ARRAY:

# APPROACH - 1

# def revARR(arr,l,r):
#   n = len(arr)
  
#   if l>=r:
#     return arr
#   arr[l],arr[r] = arr[r],arr[l]
#   return revARR(arr,l+1,r-1)

# print(revARR([1,2,3,4,5],0,1))


# APPROACH - 2


# def revArr(arr,i):
#   n = len(arr)
#   if i>=n//2:
#     return arr
#   arr[i],arr[n-i-1] = arr[n-i-1],arr[i]
#   return revArr(arr,i+1)

# print(revArr([1,2,3,4,5],0))


#___________________________________________________________________________


# CHECH THE GIVEN STRING IS POLIDROME OR NOT:

# def check_Polidrome(str,i):

#   n = len(str)

#   if i>=n//2:
#     return True

#   if str[i] != str[n-i-1]:
#     return False

#   return check_Polidrome(str,i+1)

# print(check_Polidrome("MADAM",0))


#___________________________________________________________________________


# PRINT FIBONACCI NUMBER:

# def fibo(n):

#   if n<=1:
#     return n
#   else:
#     return fibo(n-1)+ fibo(n-2)

# print(fibo(6))


#___________________________________________________________________________


# FACTOTAIL OF A NUMBER:

# def fact(n):

#   if n<=1:
#     return n

#   return n*fact(n-1)

# print(fact(5))


#___________________________________________________________________________


# CHECH GIVEN NUMBER IS IS EQUAL TO ANY POWER OF 3 OR NOT:

# def isPower(n):

#   if n == 3 or n == 1:
#     return True

#   if n != 0 and n%3 == 0:
#     return isPower(n/3)

#   return False

# print(isPower(-27))


#___________________________________________________________________________


# CHECH GIVEN NUMBER IS IS EQUAL TO ANY POWER OF 4 OR NOT:

# def isPower(n):

#   if n == 4 or n == 1:
#     return True

#   if n!=0 and n%4 == 0:
#     return isPower(n/4)

#   return False

# print(isPower(20))


#___________________________________________________________________________