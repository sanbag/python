def missing_number(arr,n):
    total_sum= n*(n+1)/2
    sum =0
    for i in arr:
        sum += i

    return total_sum-sum

print(missing_number([1, 2, 4, 5],5))