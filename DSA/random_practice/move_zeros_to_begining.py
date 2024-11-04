def move_zeros_to_begining(arr):
    pointer = 0
    for i in range(len(arr)):
        if arr[i]==0:
            arr[pointer],arr[i]=arr[i],arr[pointer]
            pointer+=1

    return arr

print(move_zeros_to_begining([1,0,0,1,3,4]))


print(move_zeros_to_begining([0, 1, 0, 2, 0, 3]))