
def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right =arr[mid:]

    left =merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left,right)
def merge_two_sorted_lists(a,b):
    len_a =len(a)
    len_b = len(b)
    i=j=0

    sorted_list =[]
    while i<len_a and j<len_b:
        if a[i]<b[j]:
            sorted_list.append(a[i])
            i+=1
        else:
            sorted_list.append(b[j])
            j+=1

    sorted_list.extend(a[i:])
    sorted_list.extend(b[j:])

    return sorted_list

print(merge_two_sorted_lists([1, 3, 4, 5, 7]
,[3, 5, 6, 7, 8]))

print(merge_sort([5,3,4,1,2,1,4]))