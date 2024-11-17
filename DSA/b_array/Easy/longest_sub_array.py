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

def longest_sub_array_hash_map(arr,k):
    sum =0
    maxlength =0

    dict={}

    for i in range(len(arr)):
        sum+=arr[i]
        if sum == k:
            maxlength = max(maxlength,i+1)

        remain = sum-k

        if sum not in dict:
            dict[sum]  =i
        print(dict)
        if remain in dict:
            length =  i - dict[remain]
            maxlength = max(maxlength,length)

    return maxlength

print(longest_sub_array_hash_map([1,2,3,1,1,1,1,4,2,3],3))