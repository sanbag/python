def selection_sort(arr):
    min = 0

    for i in range(len(arr)):
        pointer =i
        for j in range(1,len(arr)):
            if arr[j]<arr[i]:
                arr[j],arr[i]=arr[i],arr[j]
                pointer = j

    return arr


print(selection_sort([64, 25, 12, 22, 11,1]))




