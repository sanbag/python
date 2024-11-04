def move_zeros_to_end(arr):
    pointer = len(arr)-1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 0:
            arr[i], arr[pointer] = arr[pointer], arr[i]
            pointer -= 1

    return arr


print(move_zeros_to_end([1, 0, 0, 1, 3, 4]))
