# smallest index such that arr [index]>=target

def lowerbound(arr,target):
    low =0
    high =  len(arr)-1
    ans = len(arr)
    while high>= low:

        mid = (low+high)//2
        if arr[mid] >= target:
            ans = mid
            high =mid-1
        else:
            low= mid+1
    return  ans


print(lowerbound([3,5,8,15,19],19))
print(lowerbound([3, 5, 8, 15, 19], 20))  # Expected output: 5, the index where 20 would be inserted
