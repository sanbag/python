def number_that_appear_ones(arr):
    xor =0
    for i in arr:
        xor= xor^i

    print(xor)

number_that_appear_ones([1,1,2,3,3,4,4])