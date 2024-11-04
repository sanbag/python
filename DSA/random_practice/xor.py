def xor_by_dict(arr):
    l = len(arr)
    dict ={}

    for i in arr:
        dict[i] = dict.get(i,0)+1
    print(dict)

    for i in arr:
        if dict[i]==1:
            return i

def xor(arr):
    acc =0
    for i in arr:
        acc^=i
    return acc
print(xor([1,2,2,4,4,4,4]))