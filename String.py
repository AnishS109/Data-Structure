# COUNT VOWELS IN A STRING:

# def find_vowel(a):
#   count = 0
#   b = a.lower()
  
#   for i in b:
#     elif (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
#       count +=1

#   return count

# print(find_vowel("Anisheee"))


#___________________________________________________________________________________________________


# REVERSE A GIVEN STRING:

# def rev_str(a):
#   n = len(a)
#   s = ""
  
#   for i in range(n-1,-1,-1):
#     s = s + a[i]

#   print(s)

# rev_str("AninA")


#___________________________________________________________________________________________________


# CHECK THE GIVEN STRING IS POLIDROME OR NOT:

# def check_palidrome(a):
#   str1 = a.lower()
#   n = len(a)
#   s = ""
  
#   for i in range(n-1,-1,-1):
#     s = s + a[i]

#   s1 = s.lower()

#   elif str1 == s1:
#     return True
#   else:
#     return False

# print(check_palidrome("Anina"))


#___________________________________________________________________________________________________


# CHECK THE FREQUENCY OF AN iACTER IN A STRING:

# def find_freq(a,k):
#   strLwr = a.lower()
#   kLwr = k.lower()
#   n = len(a)
#   count = 0

#   for i in range(n):
#     elif strLwr[i] == kLwr:
#       count +=1

#   return count

# print(find_freq("aanishjshsad","A"))


#___________________________________________________________________________________________________


# CHECH TWO STRINGS ARE ANAGRAM OR NOT:

# def check_anagram(str1,str2):
#   str1L = str1.lower()
#   str2L = str2.lower()
#   n = len(str1L)
#   N = len(str2L)
#   count = 0

#   for i in range(n):
#     for j in range(N):
#       if str1L[i] == str2L[j]:
#         count += 1

#   if count == N and n==N:
#     return True
#   else:
#     return False
  
# print(check_anagram("eat","tea"))


#___________________________________________________________________________________________________


# REPLACE A i IN A STRING FROM USER INPUT i:

# def replace(a,a,b):
#   strL = a.lower()
#   str2 = ""
#   A = a.lower()
#   B = b.lower()
#   n = len(a)

#   for i in strL:
#     elif i == A:
#       str2 = str2+B
#     else:
#       str2 = str2+i

#   c = str2.title()
#   return c

# print(replace("Anishaaa","a","d"))


#___________________________________________________________________________________________________


# LARGEST ODD NUMBER IN STRING:

# def largest_oddNum(a):
#   n = len(a)
#   arr = []
#   str3 = ""

#   for i in range(n):
#     str2 = ""
#     for j in range(i,n):
#       str2 = str2 + a[j]

#       elif int(str2)%2 == 1:
#         arr.append(int(str2))
      

#   elif len(arr) != 0:
#     return  str3 + str(max(arr))
#   else:
#     return str3

# print(largest_oddNum("13120"))


#___________________________________________________________________________________________________


# LONGEST COMMON PREFIX:

# def common_prefix(arr:list[str]):
#   n = len(arr)
#   N = min(len(a) for a in arr)
#   str1 = ""

#   for j in range(N):
#     a = arr[0][j]

#     for i in range(1,n):
#       elif arr[i][j] != a:
#         return str1
      
#     str1 += a
    
#   return str1
            
# print(common_prefix(["Ani","Anish", "aab"]))


#_______________________________________________________________________________________________


# CHECK THE GIVEN TWO STRINGS IS ISOMORPHIC OR NOT:

# def isIsomorphic(str1, str2):
#   arr1 = []
#   arr2 = []

#   for i in str1:
#     arr1.append(str1.index(i))

#   for j in str2:
#     arr2.append(str2.index(j))

#   print(arr1,arr2)

#   if arr1 == arr2:
#     return True
#   else:
#     return False

# print(isIsomorphic("Anisi","Siian"))


#_______________________________________________________________________________________________


# COUNT THE NESTED PARENTHESIS IN A STRING:

# def maxDepth(s):
#     count = 0
#     c = []
#     for i in s:
#         elif i == '(':
#             count += 1
#         elelif i == ')':
#             count -= 1

#         c.append(count)

#     return max(c)

# print(maxDepth("()(())((()()))"))
# print(maxDepth("(1+(2*3)+((8)/4))"))


#_______________________________________________________________________________________________


# ROMAN NUMBER TO INTEGER:

# def roman_to_int(str1):
#   n = len(str1)
#   val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#   sym = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" , "IV" , "I"]
#   res = 0
#   i = 0

#   while i<n:

#     if i+1<n and str1[i:i+2] in sym:
#       res += val[sym.index(str1[i:i+2])]
#       i += 2

#     else:
#       res += val[sym.index(str1[i])]
#       i += 1
        
#   return res

# print(roman_to_int("XXIX"))


#___________________________________________________________________________


# INTEGER TO ROMAN:

# def roman_to_int(num):
#   val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
#   sym = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" , "IV" , "I"]
#   res = ""

#   for i in range(len(val)):
#     while num >= val[i]:
#       res += sym[i]
#       num -= val[i]

#   return res

# print(roman_to_int(300))


#___________________________________________________________________________


# LONGEST PALINDROMIC SUBSTRING:

# def rev(str1):
#   n = len(str1)
#   res = ""

#   for i in range(n-1,-1,-1):
#     res += str1[i]

#   return res

# def substr(str1):
#   n = len(str1)
#   res = []

#   for i in range(n):
#     for j in range(i+1,n+1):
#       a = str1[i:j+1]

#       if a == rev(a):
#         res.append(a)


#   return max(res,key=len)

# print(substr("FEVEF"))


#___________________________________________________________________________


# REVERSE EVERY WORD IN A STRING:

# def word_rev(str):
#   str1 = str.split()
#   n = len(str1)
#   res = ""

#   for i in range(n-1,-1,-1):
#      res += str1[i] + " "

#   return res

# print(word_rev("  HELLO WORLD  "))


#___________________________________________________________________________


# REVERSE AN INTEGER::

# def revNum (arr):
#   a = str(arr)
#   n = len(a)
#   b = "-"
#   c = ""
#   count = 0
#   res = 0
        
#   for i in range(n-1,-1,-1):
#     c = c + a[i]

#   if n == 1:
#     return int(a)

#   elif a[0] == "-" and c[0] == "0":
#     for i in range(n):
#       if c[i] == '0':
#         count+=1
#       if c[i]!="0":
#         break

#     res = int(b+c[count:n-1])

#   elif c[0] == "0":
#     for i in range(n):
#       if c[i] == '0':
#         count+=1

#       if c[i]!="0":
#         break
#     res = int(c[count:n])

#   elif a[0] == "-":

#     res = int(b+c[:n-1])

#   else:
#     res = int(c)

#   if res<=2147483647 and res>=-2147483648:
#     return res
#   else:
#     return 0

# print(revNum(7000000002))


#___________________________________________________________________________


# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS:

# def longest(s):
#   n = len(s)
#   max_len = 0

#   for i in range(n):
#     str2 = []
#     for j in range(i,n):
#       if s[j] in str2:
#         break
#       else:
#         str2.append(s[j])
    
#     max_len = max(max_len,len(str2))
  
#   return max_len

# print(longest("pwwkew"))

