// ----------------------------- REMOVE OUTERMOST PARANTHESIS ------------------------

const outerParan = (s) => {
    let n = s.length
    let c=0
    let i = 0
    let mapi = {}
    let ans = ""
  
    while(i<=(n-1)){
  
      if(i==0){
        mapi[i] = -1
        i+=1
        c+=1
      }
  
      if(s[i] == "("){
        c+=1
        mapi[i] = c
        i+=1
      } else {
        c-=1
  
        if(c!=0){
          mapi[i]=c
          i+=1
        } else {
          mapi[i] = 0
          mapi[i+1] = -1
          c+=1
          i+=2
        }
      }
    }
  
    for(let i = 0;i<n;i++){
      if(mapi[i] != -1 && mapi[i] != 0){
        ans = ans+s[i]
      }
    }
  
    return ans
  }
  
  
  // ------------------------------ REVERSE WORDS IN STRING --------------------------

  let reverseWord = (str) => {
    let s = str.split(" ")
    let ans = ""

    for(let i = (s.length-1);i>-1;i--){
      if(s[i] != ""){

        ans = ans+s[i]+" "
      }
    }
    return ans.trim()
  }


  // ----------------------------- LARGEST COMMON PREFIX ------------------------

  const commonPrefix = (s) => {
  s.sort()
  let str1 = s[0]
  let str2 = s[s.length - 1]
  let n = str1.length
  let ans = ""

  for(let i=0;i<n;i++){
      if(str1[i] == str2[i]){
          ans = ans+str1[i]
      } else {
          return ans
      }
  }
  return ans
  }

  // -------------------------------- ISOMORPHIC STRING -----------------------------

  const isIsomorphic = (s,t) => {
      let ans1 = []
      let ans2 = []

      for(let i in s){
          ans1.push(s.index(i))
      }

      for(let j in t){
          ans2.push(t.index(j))
      }

      if(ans1 == ans2){
          return true
      } else {
          return false
      }
  }

  // --------------------------- CHECK ONE STRING IS ROATATION OF ANOTHER --------------------------

  const checkRotation = (s,t) => {
      let n = s.length

      if (n != t.length){
          return false
      }

      for(let i=0;i<n;i++){
          let temp = Array(n)

          for(let j=0;j<n;j++){
              temp[(j+i)%n] = s[j]
          }

          if(temp.join("") == t){
              return true
          }
      }

      return false
  }

  // ------------------------------ VALID ANAGRAM -----------------------------

  const validAnagram = (s,t) => {
      let n = s.length

      if (n != t.length){
          return false
      }

      let ans1 = {}
      let ans2 = {}

      for(let i =0;i<n;i++){

          if(s[i] in ans1){
              ans1[s[i]] += 1
          } else{
              ans1[s[i]] = 1
          }

          if(t[i] in ans2){
              ans2[t[i]] += 1
          } else {
              ans2[t[i]] = 1
          }
      }

      if(ans1 == ans2){
          return true
      } else {
          return false
      }
  }

  // --------------------------------- BEAUTY SUM -------------------------------

  const beautySum = (s) => {
    let n = s.length
    let total = 0

    for(let i=0;i<n;i++){
      let ans = {}
      for(let j=i;j<n;j++){

        if(s[j] in ans){
          ans[s[j]] += 1
        } else {
          ans[s[j]] = 1
        }

        let values = Object.values(ans)

        let maxi = Math.max(...values)
        let mini = Math.min(...values)
        total += maxi-mini

      }
    }
    return total
  }

  // ---------------------------------- REVERSE WORDS -----------------------------
  
  const revrseWords = (s) => {
    let a = s.split()
    let n = a.length
    ans = []

    for(let i=0;i<n;i++){
      ans.push(a[n-1-i])
    }

    return ans.join(" ")
  }

  