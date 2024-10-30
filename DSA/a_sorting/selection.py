def selection_sort(arr):
    for i in range(len(arr)):
        min =i
        for j in range(1+i,len(arr)):
            if arr[j]<arr[min]:
                min=j

        arr[i],arr[min]= arr[min],arr[i]

    return arr

print(selection_sort([64, 25, 12, 22, 11,1]))
