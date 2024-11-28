def buy_sell_stock(arr):
    min_value = arr[0]
    min_index = 0  # To track the index of the minimum value
    max_diff = float("-inf")
    start_day = -1
    end_day = -1

    for i in range(1, len(arr)):
        diff = arr[i] - min_value
        if diff > max_diff:
            max_diff = diff
            start_day = min_index  # Start day is where the min_value occurred
            end_day = i
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i  # Update the index of the new minimum value

    return max_diff, start_day, end_day


print(buy_sell_stock([7, 2, 5, 6, 3, 6, 4,1,9]))
