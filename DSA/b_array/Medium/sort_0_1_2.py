def sort_0_1_2 (arr):
    low =0
    mid= 0
    high = len(arr)-1


    while mid<high:

        if arr[mid] == 0:
            arr[low],arr[mid]= arr[mid],arr[low]
            low+=1
            mid+=1

        if arr[mid]==1:
            mid = mid+1

        if arr[mid] ==2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high-=1
        print(arr)

    return  arr

print(sort_0_1_2([0,0,0,1,0,1,2,1]))