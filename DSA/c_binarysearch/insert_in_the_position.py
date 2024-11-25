from tkinter.font import names


def inser_in_position(arr,tar):

    low =0
    high= len(arr)-1
    ans =0

    while high>=low:
        mid = (low+high)//2

        if arr[mid] == tar:
            return  arr

        elif arr[mid]>=tar:
            ans = mid
            high = mid-1

        else:
            low =  mid+1

    return arr[:ans] + [tar] + arr[ans:]

print( inser_in_position([1, 2,3,3, 4, 7],6))