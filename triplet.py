

def find_3_indices(arr):
    n = len(arr)
    if n< 3:
        return []

    Smaller = [-1] * n
    Larger = [-1] * n

    min_index = 0
    for i in range(1, n):
        if arr[i] > arr[min_index]:
            Smaller[i] = min_index
        else:
            min_index = i

    # print(min_index)
    # print(list(Smaller))

    max_index = 0
    for i in range(n-2, -1, -1):
        if arr[i] < arr[max_index]:
            Larger[i] = max_index
        else:
            max_index = i

    # print(max_index)
    # print(list(Larger))

    for j in range(n):
        if Smaller[j] != -1 and Larger[j] != -1:
            i = Smaller[j]
            k = Larger[j]
            return [i, j, k]


    return []




arr = [2, 5, 3, 1, 4, 9, 6]
result = find_3_indices(arr)
print("Indices i, j, k are:", result)