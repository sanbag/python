def two_sum(l,t):
    prev_map ={}

    for i,n in enumerate(l):
        diff =t-n
        if diff in prev_map:
            return [prev_map[diff],i]

        prev_map[n]=i
    return

print(two_sum([3,4,5,6],7))


