def two_sum(arr,target):
    det ={}

    for index,value in enumerate( arr):
        diff = target-value
        if diff in det:
            return (det[diff],index)
        else:
            det[value] =index

print(two_sum([1,2,3,4,5,6,7],7))