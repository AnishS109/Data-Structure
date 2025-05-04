// ---------- FINDING LARGE ELEMENET IN ARRAY  ---------


const Large_Element = (arr) => {
  let n = arr.length
  let maxi = arr[0]

  for (let i = 1; i<n ; i++){
    if(arr[i]>maxi){
      maxi = arr[i]
    }
  }

  return maxi
}


// --------- FINDING SECOND LARGEST -------------


const Second_Largest = (arr) => {
  let n = arr.length;
  let SL =  -Infinity;
  let L = -Infinity;

  for(let i = 0; i<n ; i++){
    if(arr[i]>L){
      SL = L
      L = arr[i]
    }
    if(arr[i]>SL && arr[i]<L){
      SL = arr[i]
    }
  }

  return SL
}


// ------------ REMOVING DUPLICATES FROM ARRAY ----------------


const removeDuplicates = (arr) => {
  let n = arr.length;
  let count = 0;
  let Arr2 = [];

  for (i=0;i<n;i++){
    if(!Arr2.includes(arr[i])){
      Arr2.push(arr[i])
    }
    else {
      count += 1
    }
  }
  return Arr2.length == 0 ? arr : Arr2
}


// ----------- ROTATE ARRAY ----------------


const rotateArray = (arr,k) => {
  let n = arr.length;
  let arr2 = []

  for (let i=0; i<k ; i++){
    let val = arr.pop();
    arr2.unshift(val)
  }

  return [...arr2, ...arr]
}


// ----------- MOVING ZEROES TO END -----------------


const movingZero = (arr) => {
  let n = arr.length
  let arr2 = []
  let count = 0

  for (let i = 0; i < n; i++){
    if(arr[i] != 0){
      arr2.push(arr[i])
    }
    else {
      count += 1
    }
  }
  for (let i = 0; i<count; i++){
    arr2.push(0)
  }

  return arr2
}


// ---------- LINEAR SEARCH --------------


const linearSearch = (arr,k) => {
  let n = arr.length

  for (let i=0; i<n ; i++){
    if (arr[i] == k){
      return true
    }
  }

  return false
}


// --------- UNION OF TWO SORTED ARRAY -----------


const Union = (a,b) => {
  let na = a.length;
  let nb = b.length;
  let i = 0 
  let j = 0
  let ans = []

  while (i<na && j<nb) {

    if (a[i] < b[j]){
      if(ans.length == 0 || ans[ans.length - 1] != a[i]){
        ans.push(a[i])
      }
      i += 1
    }
    else if (a[i] > b[j]){
      if (ans.length == 0 || ans[ans.length - 1] != b[j]){
        ans.push(b[j])
      }
      j += 1
    }
    else {
      if (ans.length == 0 || ans[ans.length - 1]!= a[i]){
        ans.push(a[i])
      }
      i += 1
      j += 1
    }
  }

  while (i < na){
    if (ans.length == 0 || ans[ans.length - 1] != a[i]){
      ans.push(a[i])
    }
    i += 1
  }

  while (j < nb){
    if (ans.length == 0 || ans[ans.length - 1] != b[j]){
      ans.push(b[j])
    }
    j += 1
  }

  return ans
}


// --------- MISING NUMBER IN ARRAY ---------------


const missing = (arr) => {
  n = arr.length

  for (let i = 0; i < n; i++){
    if(!arr.includes(i+1)){
      return i+1
    }
  }
}


// ---------- MAXIMUM CONSECUTIVES ONES ----------


const consOnes = (arr) => {
  n = arr.length;
  count = 0
  maxCount = -1

  for (let i = 0 ; i<n ; i++){
    if (arr[i] == 1){
      count += 1

      if(count > maxCount){
        maxCount = count
      }
    }
    else {
      count = 0
    }
  }

  return maxCount == -1 ? 0 : maxCount
}


// ------------ FIND SINGLE NUMBER ----------------


const findSingleNum = (nums) => {
  n = nums.length
  count = 0

  for(let i = 0; i<n ; i++){
    for(let j = i+1; j<n; j++){
      if(nums[i] == nums[j]){
        count += 1
        console.log(count);
      }
    }
    if(count == 0){
      return nums[i]
    } else {
      count = 0
    }
  }
}


// ----------- LONGEST SUBARRAY WITH GIVEN SUM  ------------

// ------------ (PENDING) --------------

const  longestSubArray = (arr, k) => {
  n = arr.length
  numMap = {}
  sum = 0
  l = 0

  for(let i=0; i<n; i++){
    sum += arr[i]
    a = k - sum
    if(a in numMap){
      l = i+1
    }

    numMap[arr[i]] = i
  }
  return l
}


// --------------- TWO SUM ----------------


const twoSum = (nums, target) => {
  let n = nums.length
  let ans = []
  for(let i=0; i<n; i++){
    for(let j = i+1; j<n; j++){
      if(nums[i] + nums[j] == target){
        ans.push(i)
        ans.push(j)
      }
    }
  }
  return ans
}

const optimizedTwoSum = (arr,target) => {
  let n = arr.length
  let numMap = {}

  for(let i=0; i<n; i++){
    a = target - arr[i]

    if(a in numMap){
      return [numMap[a], i]
    }
    numMap[arr[i]] = i
  }
}

// ---------------- SORT COLORS ------------------

const sortColors = (nums) => {
  let n = nums.length
  let zero = 0
  let one = 0
  let two = 0
  let arr = []

  for(let i=0;i<n;i++){

    if(nums[i] == 0){
      zero += 1
    } else if( nums[i] == 1){
      one += 1
    } else {
      two += 1
    }
  }

  for(let i=0;i<n;i++){

    if(zero>0){
      arr.push(0)
      zero -= 1
    }
    else if(one>0){
      arr.push(1)
      one -= 1
    }
    else{
      arr.push(2)
      two -= 1
    }
  }

  return arr
}


// ------------------ MAJORITY ELEMENT (n/2) -----------------

const majority = (nums) => {
  
}


// --------------------- MAXIMUM SUBARRAY ----------------------

const maxSubArray = (nums) => {
  n = nums.length
  arr = []

  for(let i=0;i<n;i++){
    for(let j=i+1;j<n;j++){
      let sum = 0

      for(let k=i;k<j;k++){
        sum += nums[k]
      }
      arr.push(sum)
    }
  }

  let max = arr[0]
  
  for(let i=0; i<arr.length; i++){
    if(arr[i] > max){
      max=arr[i]
    }
  }

  return max
}

const optimizeMaxSubArray = (nums) => {
  let n = nums.length 
  let maxi = -Infinity
  let sum = 0

  for(let i=0;i<n;i++){
    sum+=nums[i]
    if(sum>maxi){
      maxi = sum
    }

    if(sum < 0){
      sum = 0
    }
  }
  return maxi
}

// ------------ RE-ARRANGE ELEMENTS BY SIGN ------------------

const bySign = (arr) => {
  let n = arr.length
  let posi = []
  let negi = []

  for(let i=0;i<n;i++){
    if(arr[i] > 0){
      posi.push(arr[i])
    } else {
      negi.push(arr[i])
    }
  }

  let posiIndex =  0
  let negiIndex =  0

  for(let i=0;i<n;i++){
    if(i%2 == 0){
      arr[i] = posi[posiIndex]
      posiIndex+=1
    } else {
      arr[i] = negi[negiIndex]
      negiIndex+=1
    }
  }
  return arr
  
}

// ------------------- FIND LEADERS --------------------

const findLeader = (nums) => {
  let n = nums.length
  let arr =  [nums[n-1]]
  for(let i=(n-2);i>=0;i--){
    let leader = true
    for(let j=(i+1);j<n;j++){
      if(nums[i]<nums[j]){
        leader = false
      }
    }
    if (leader == true){
      arr.push(nums[i])
    }
  }

  return arr.reverse()
}

const optimizeFindLeader = (nums) => {
  let n = nums.length
  let prevLeader = nums[n-1]
  let arr = [nums[n-1]]

  for(let i=(n-2);i>=0;i--){
    if(prevLeader<nums[i]){
      arr.push(nums[i])
      prevLeader = nums[i]
    }
  }
  return arr.reverse()
}

// ----------------- LONGEST SUB-ARRAY WITH GIEN SUM --------------------

const subArray = (nums,k) => {
  let n = nums.length
  let preSum = {}
  let maxLen = 0
  let sum = 0

  for(let i = 0;i<n;i++){
    sum += nums[i]
    if(sum == k){
      maxLen = Math.max(maxLen,i+1)
    }

    let rem = sum - k

    if (rem in preSum){
      let a = i - preSum[rem]
      maxLen = Math.max(maxLen,a)
    }
    preSum[sum] = i
  }

  return maxLen
}


// ------------------ MAJORITY ELEMENT (N/3) ------------------------

const majority2 = (nums) => {
  let n = nums.length
  let maps = {}
  let ans = []

  for(let i=0;i<n;i++){

    if(nums[i] in maps){
      maps[nums[i]] += 1
    } else {
      maps[nums[i]] = 1
    }
  }

  for(let key in maps){
    if(maps[key] > (n/3)){
      ans.push(Number(key))
    }
  }
  return ans
}

// --------------------- FIND MISSING AND REPEATING ELEMENT -----------------------

const find = (arr) => {
  let arr1 = arr.sort((a,b) => a-b)
  let n = arr1.length
  let miss = 0
  let repeat = 0

  for(let i=0;i<n-1;i++){
    if( arr1[i] == arr1[i+1]){
      repeat = arr1[i]
    } 
    else if(arr1[i]+1 !== arr1[i+1]) {
      miss = arr1[i]+1
    }
  }
  return [miss,repeat]
}

const findOptimize = (arr) => {
  let num = {}
  let n = arr.length
  let repeat = 0
  let miss = 0

  for(let i=0; i<n; i++){
    if (arr[i] in num){
      num[arr[i]] += 1
    } else {
      num[arr[i]] = 1
    }
  }

  for (let i=1;i<=n;i++){
    if(!(i in num)){
      miss = i
    } 
    else if (num[i] > 1){
      repeat = i
    }
  }

  return [miss,repeat]
}