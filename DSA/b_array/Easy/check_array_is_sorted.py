def array_is_sorted(arr):

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False

    return True


print(array_is_sorted([1,1,2,3,4,5]))



