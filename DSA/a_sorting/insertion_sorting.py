def insertion_sorting(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j =i-1
        while j>=0 and arr[j]>key:
                
