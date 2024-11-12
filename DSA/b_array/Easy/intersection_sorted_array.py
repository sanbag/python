def intersection_array(arr1,arr2):
    a1=0
    a2=0

    intersection =[]

    while (a1 <len(arr1)  and a2 <len(arr2)):
        if arr1[a1] != arr2[a2]:
            a1+=1
        else:
            intersection.append(arr1[a1])
            a1+=1
            a2+=1
    return intersection
arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]

print(intersection_array(arr1, arr2))

