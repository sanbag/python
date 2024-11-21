def majority_element(arr):
    maj_ele =arr[0]
    count =1
    for i in range(1,len(arr)):
        if count ==0:
            maj_ele=arr[i]

        if arr[i] == maj_ele:
            count +=1
        else:
            count -=1

    return maj_ele


print(majority_element([2,1,1,3,1,2]))
print('Hi')