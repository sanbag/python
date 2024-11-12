def missing_number(arr,n):
    total_sum= n*(n+1)/2
    sum =0
    for i in arr:
        sum += i

    return total_sum-sum

print(missing_number([1, 2, 4, 5],5))

def xor_missing_number(arr,n):
    xor1 =0
    xor2 =0

    for i in range(n+1):
        xor1=xor1 ^i

    for i in arr:
        xor2 = xor2^i

    return xor1^xor2

print(xor_missing_number([1, 2, 4, 5],5))