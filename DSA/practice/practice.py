def max_sub_array(arr):
    maximum_sum = float("-inf")
    sum =0
    start_index = -1
    end_index = -1
    tem_start_index = -1
    for i in range(len(arr)):
        if sum == 0:
            tem_start_index = i
        sum += arr[i]


        if sum > maximum_sum:
            maximum_sum =sum
            start_index = tem_start_index
            end_index = i

        if sum <0:
            sum = 0
    return  maximum_sum,start_index,end_index

print(max_sub_array([-2,-3,4,-1,-2,1,7,-3,-1,-10,-1]))