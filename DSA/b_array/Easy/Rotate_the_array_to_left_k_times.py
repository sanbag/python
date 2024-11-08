def rotate_the_array(arr,k):

    while k>0:
        final = arr[len(arr)-1]
        print(final)

        for i in range(len(arr)-2,-1,-1):
            arr[i+1]= arr[i]
        arr[0]= final
        k -=1

    return arr

print(rotate_the_array([1,2,3,4,5,6,7],3))


san =[1,2,3,4,5,6,7]
ans =[7,1,2,3,4,5,6]