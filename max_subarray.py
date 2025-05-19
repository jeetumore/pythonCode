#
# def max_subarray(arr):
#     maxsum= arr[0]
#     currentsum = arr[0]
#
#     for num in arr[1:]:
#         currentsum = max(num, currentsum+ num)
#         maxsum = max(currentsum, maxsum)
#
#     print(maxsum)
#
# array= [-2,1,-3,4,-1,2,1,-5,4]
#
# max_subarray(array)

def nonDivisibleSubset(k, s):

    remainder_count = [0] * k


    for num in s:
        remainder = num % k
        remainder_count[remainder] += 1


    subset_size = min(remainder_count[0], 1)
    print(subset_size)
    print(remainder_count)

    for i in range(1, (k // 2) + 1):
        if i != k - i:  # Don't double-count when k is even and i == k-i
            subset_size += max(remainder_count[i], remainder_count[k - i])
        else:
            # If k is even and i == k-i, we can only take one number from this group
            subset_size += min(remainder_count[i], 1)

    print(subset_size)
s = [1, 7, 2, 4]
k = 3

nonDivisibleSubset(k, s)