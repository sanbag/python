def max_sub_array(arr):
    maximum_sum =  float('-inf')
    sum =0

    for i in arr:
        sum +=i
        maximum_sum = max(maximum_sum,sum)
        if sum<0:
            sum =0

    return  maximum_sum
print(max_sub_array([-2,-3,4,-1,-2,1,7,-3]))