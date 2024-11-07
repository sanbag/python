
def remove_dupliacates_from_sorted_array_brute(arr):
    if not  arr:
        return 0

    unique = list(set(arr))

    for i in range(len(unique)):
        arr[i] = unique[i]
    print(unique,arr)

    arr[:len(unique)] = unique
    print(arr)

san = [1,1, 2, 2, 2, 2, 3, 3, 3]
def remove_duplcates_optimal(arr):
    pointer = 0
    for i in range(1,len(arr)):

        if arr[i] != arr[pointer]:
            pointer += 1
            arr[pointer]=arr[i]

    print(arr)

remove_duplcates_optimal([1,1,1,2,2,3,3,4,5])




