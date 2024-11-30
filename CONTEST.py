# MINIMUM DIVISION OPERATIONS TO MAKE ARRAY NON DECREASING:

def minOperations(nums):
  n = len(nums)
  c = 0
  a = sorted(nums)

  for i in range(n-1):
            
    for j in range(2,nums[i]):
      if nums[i]%j==0:
        nums[i] = j
        c+=1

  if c == 0 and nums != a:
    return -1
  return c


#___________________________________________________________________________


# COUNT SUBSTRINGS WITH K-FREQUENCY CHARACTERS:

def numberOfSubstrings(s, k):
  n = len(s)
  final_count = 0
  a = []

  for i in range(n):
    count = 1

    if count == k:
      final_count += 1
      a.append(s[i])

    for j in range(i + 1, n):
      if k == 1:
        a.append(s[i:j + 1])
      else:
        if count == k:
          final_count += 1

        if s[i] == s[j]:
          count += 1
          if count == k:
            final_count += 1

  if k == 1:
    return len(a)

  return final_count