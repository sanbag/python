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


def using_two_pointer(arr1,arr2):
    a1 =0
    a2= 0
    union =[]

    while (a1 <len(arr1)  and a2 <len(arr2)):
        if arr1[a1]<=arr2[a2]:
            if len(union) ==0 or union[-1] != arr1[a1]:
                union.append(arr1[a1])
            a1+=1

        else:

            if  len(union) ==0 or union[-1] != arr2[a2]:
                union.append(arr2[a2])
            a2+=1

    while(a1<len(arr1)):
        if  union[-1] != arr1[a1]:
            union.append(arr1[a1])
        a1+=1

    while (a2 < len(arr2)):
        if union[-1] != arr2[a2]:
            union.append(arr2[a2])
        a2 += 1

    return union

print(using_two_pointer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],[2, 3, 4, 4, 5, 11, 12]))

