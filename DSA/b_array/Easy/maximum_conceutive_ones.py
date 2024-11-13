def maximun_conceutive_ones(arr):
    ones =0
    current_ones = 0
    for i in arr:
        if i ==1 :
            current_ones +=1
        else :
            ones = max(ones,current_ones)
            current_ones = 0

    return ones

print(maximun_conceutive_ones([1,0,1,1,1,1,0,1]))