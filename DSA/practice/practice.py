def move_zero_to_end(arr):
    l=len(arr)-1
    for i  in range(len(arr)-1,-1,-1):
        if arr[i]==0:
            arr[l],arr[i]=arr[i],arr[l]
            l-=1

    return arr
print(move_zero_to_end([1,0,0,1,1,0,1,1,1,0]))

def move_zero(arr):
    l=0
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[i],arr[l]=arr[l],arr[i]
            l+=1
    return arr
print(move_zero([1,0,0,1,1,0,1,1,1,0]))