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


# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------





# ------------------------------------ FACTORIAL OF A NUMBER -------------------------------


def factorial(n):

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


# -------------------------------------- FIBONACCI SERIES ----------------------------------


def fibonacci_Series(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_Series(n-2) + fibonacci_Series(n-1)
    

# ------------------------------------- SUM OF ALL ELEMENTS IN ARRAY ---------------------------


def sum(arr,n):

    if n == 0:
        return 0
    else:
        return sum(arr,n-1) + arr[n-1]
    

# -------------------------------------- PRINT 1 to N -------------------------------------


def print_one(n):
    if n == 0:
        return 0
    else:
        print_one(n-1)
        print(n)


# -------------------------------------- PRINT N to 1 -------------------------------------


def print_rev(n):
    if n == 0:
        return 0
    else:
        print(n)
        print_rev(n-1)


# ----------------------- NUMBER  OF WAYS TO CLIMB STAIRS -------------------------------


def climb_stairs(n):
    if n == 0:
        return 1
    elif n<0:
        return 0
    else:
        return climb_stairs(n-1) + climb_stairs(n-2)
    

# ------------------------ REVERSE AN ARRAY ------------------------------


def reverse(arr,i):
    n = len(arr)

    if i > n//2:
        return arr
    
    arr[i],arr[n-1-i] = arr[n-1-i],arr[i]
    return reverse(arr,i+1)


# -------------------------- CHECK STRING PALINDROME -----------------------------


def check_palindrome(s,i):
    n = len(s)
    if i > n//2:
        return True
    else:
        if s[i] != s[n-1-i]:
            return False
        return check_palindrome(s,i+1)


# --------------------------- CONVERT STRING INTO INTEGER ----------------------------


def string_to_int(s):
    i = 0
    strr = s.strip()
    ans = ""
    n = len(strr)

    if i<n and (strr[i] == "-" or strr[i] == "+"):
        ans += strr[i]
        i += 1

    def helper(i, ans):
        if i == n or not strr[i].isdigit():
            return ans
        ans += strr[i]
        return helper(i+1,ans)
    
    ans = helper(i,ans)

    num = int(ans)
    mini = -2**31
    maxi = 2**31 - 1

    if num>maxi:
        return maxi
    elif num<mini:
        return mini
    
    return num


# ----------------------------- POWER of X,N ---------------------------------


def myPow(x,n):
    if n == 0:
        return 1
    if n<0:
        return 1 / myPow(x,-n)
    half = myPow(x,n//2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
    

# ------------------------------- RETURN NUMBER OF GOOD NUMBERS --------------------------------

# BRUTE FORCE :
def count_good(n):

    def powers(base,x,mod):
        if x == 0:
            return 1
        else:
            return (base * powers(base,x-1,mod)) % mod

    MOD = 10 ** 9 + 7
    even_pos = (n+1) // 2
    odd_pos = n // 2
    even_ans = powers(5,even_pos,MOD)
    odd_ans = powers(4,odd_pos,MOD)
    return (even_ans * odd_ans) % MOD


# OPTIMIZE :
def count_good_optmized(n):
    def powers(base,x,mod):
        if x == 0:
            return 1
        half = powers(base,x//2,mod)
        result = (half * half) % mod
        if x % 2 == 1:
            result = (result * base) % mod
        return result
    
    MOD = 10**9 + 7
    even_pos = (n+1) // 2
    odd_pos = n//2
    even_ans = powers(5,even_pos,MOD)
    odd_ans = powers(4,odd_pos,MOD)
    return (even_ans * odd_ans) % MOD


# -------------------------------- GENERATE PARANNTHESIS ------------------------------------


def generate_paren(n):

    def backTrack(s,ans,open_count,close_count):
        if len(s) == n*2:
            ans.append(s)
            return
        if open_count < n:
            backTrack(s + "(",ans,open_count + 1,close_count)
        if close_count < open_count:
            backTrack(s + ")", ans, open_count, close_count + 1)
        
    ans = []
    open_count = 0
    close_count = 0
    backTrack("",ans,open_count,close_count)
    return ans


# ------------------------------- PRINT ALL SUBSEQUENCE ------------------------------


def all_sub(arr):

    def backTrack(arr,ans,i,output):
        if i >= len(arr):
            ans.append(output[:])
            return
        
        # exclude
        backTrack(arr,ans,i+1,output)

        # include
        output.append(arr[i])
        backTrack(arr,ans,i+1,output)
        output.pop()

    ans = []
    i = 0
    output = []
    backTrack(arr,ans,i,output)
    return ans
