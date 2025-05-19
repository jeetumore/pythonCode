

# def insertionSort1(n, arr):
#     # Write your code here
#     value = arr[n -1]
#     n = n - 1
#     while (n > 0):
#         if value < arr[n - 1]:
#             temp = arr[n - 1]
#             arr[n] = temp
#         else:
#             arr[n] = value
#         print(' '.join((map(str, arr))))
#         n -= 1
#
# insertionSort1(5, [2, 4, 6, 8, 3])







def sortingArray(arr):
    n = len(arr)

    for i in range(n):
        middle_Index = i
        for j in range(i+1, n):
            if arr[j] < arr[middle_Index]:
                middle_Index = j
        arr[middle_Index], arr[i] = arr[i], arr[middle_Index]

    print(arr)


arr=[7, 9, 9, 3, 4, 6, 8, 2]

sortingArray(arr)





