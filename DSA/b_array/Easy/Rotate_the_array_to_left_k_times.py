def rotate_the_array_brute_force(arr,k):

    while k>0:
        final = arr[len(arr)-1]
        print(final)

        for i in range(len(arr)-2,-1,-1):
            arr[i+1]= arr[i]
        arr[0]= final
        k -=1

    return arr

# print(rotate_the_array_brute_force([1,2,3,4,5,6,7],3))

def rotate_the_array_slicing(arr,k):
    n= len(arr)

    arr = arr[-k:]+arr[:-k]
    return arr

print(rotate_the_array_slicing([1,2,3,4,5,6,7],3))

def rotate_the_array_better(arr):
    emp =[]





