def using_sets(arr1,arr2):
    unique =set()

    for num in arr1:
        unique.add(num)
    for num in arr2:
        unique.add(num)

    print( list(unique))

using_sets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[2, 3, 4, 4, 5, 11, 12])

def using_dicts(arr1,arr2):
    dict={}
    uniqe =[]
    for num in arr1:
        dict[num] = dict.get(num,0)+1
    for num in arr2:
        dict[num] = dict.get(num, 0) + 1

    for num in dict:
        uniqe.append(num)

    print(uniqe)
using_dicts([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[2, 3, 4, 4, 5, 11, 12])

