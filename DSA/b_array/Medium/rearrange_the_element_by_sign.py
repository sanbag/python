def rearrange_the_element_by_array(arr):
    pos_pointer =0
    neg_pointer = 1

    rearrange_array = [0]*len(arr)

    for i in arr:
        if i >0:
            rearrange_array[pos_pointer] = i
            pos_pointer+=2

        else:
            rearrange_array[neg_pointer]=i
            neg_pointer +=2

    return rearrange_array

print(rearrange_the_element_by_array([3,1,-2,4,-5,-6]))

def rearrange_the_element_by_array_second_type(arr):
    possitive =[]
    negative =[]

    for i in arr:
        if i>0:
            possitive.append(i)
        else:
            negative.append(i)

    equal_length = min(len(possitive),len(negative))

    sorted =[]
    for i in range(equal_length):
        sorted.append(possitive[i])
        sorted.append(negative[i])

    if len(possitive)>equal_length:
        sorted.extend(possitive[equal_length:])
    else:
        sorted.extend(negative[equal_length:])

    return sorted

print(rearrange_the_element_by_array_second_type([3,2,1,-2,-4,-5,-6]))