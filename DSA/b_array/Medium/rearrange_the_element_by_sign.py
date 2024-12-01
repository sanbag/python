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