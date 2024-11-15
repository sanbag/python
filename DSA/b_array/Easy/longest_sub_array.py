def longest_sub_array_brute(arr,k):
    longest = 0
    for i in range(len(arr)):
        if arr[i]<k:
            sum =0
            count =0
            for j in range(i,len(arr)):
                if sum<k:
                    sum += arr[j]
                    count +=1
                else:
                    longest = max(longest,count)

    return longest




print(longest_sub_array_brute([1,2,3,1,1,1,1,4,2,3],4))