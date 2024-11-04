# we move maximum element at the end
def bubble_sort(arr):
    n =len(arr)

    for i in range(n):
        print(i)
        swap = False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap = True

        if  swap == False:
            return arr


    return arr

arr = [11, 12, 22, 25, 34, 64, 90]
# arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)