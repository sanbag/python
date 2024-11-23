# smallest index such that arr [index]>target



def upperbound(arr,target):
    low = 0
    high = len(arr)-1
    ans = len(arr)

    while high>= low:
        mid = (low+high)//2

        if arr[mid] <= target:
            low = mid+1

        else:
            ans = mid
            high = mid-1
    return ans

print(upperbound([3, 5, 8,8,8,8, 15, 19],8 ))
print(upperbound([3, 5, 8, 8, 8, 8, 15, 19], 8))  # Expected output: 6
print(upperbound([3, 5, 8, 15, 19], 1))  # Expected output: 0
print(upperbound([3, 5, 8, 15, 19], 20))  # Expected output: 5 (since target > all elements)
