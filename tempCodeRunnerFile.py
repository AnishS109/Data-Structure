def search(arr,x):
    low = 0
    high = len(arr)-1
    ans1 = 0

    while low<=high:
        
        mid = (low+high)//2

        if arr[mid] <= x:
            ans1= mid
            low = mid + 1

    return ans1
print(search([1,3,7,5],6))