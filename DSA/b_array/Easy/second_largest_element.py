def find_second_largest(arr):
    if len(arr)<2:
        return None

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num

        elif first>num>second:
            second = num

    return second if second != float('-inf') else None

print(find_second_largest([10, 20, 4, 45, 99]))