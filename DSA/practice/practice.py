def binary_insert (arr,k):
        l =0
        r =len(arr)-1

        while  l<r:
            mid = (l+r)//2

            if arr[mid] ==k:
                return mid

            elif arr[mid]>k:
                r = mid-1

            else:
                l = mid+1

        return l

print(binary_insert([1,2,4,7],1))