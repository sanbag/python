from codecs import make_identity_dict


def binary_search(arr,target):
    low = 0
    high =  len(arr)-1

    while high>=low:
        mid = (low+high)//2

        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            low =mid+1
        else:
            high = mid-1
    return  -1

print(binary_search([1,2,3,4,5,6,7,8],8))

def binary_search_recursive(arr,low,high,target):
    if low>high:
        return -1

    mid = (low+high)//2
    if arr[mid] == target:
        return mid
    elif target>arr[mid]:
        return binary_search_recursive(arr,mid+1,high,target)
    return binary_search_recursive(arr,low,mid-1,target)

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search_recursive(arr, 0, len(arr) - 1, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")
