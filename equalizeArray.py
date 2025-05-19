from collections import Counter


# def equalizeArray(arr):
#     array = []
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] not in array and arr[i] == arr[j]:
#                 array.append(arr[i])
#
#
#     print(array)
#



def equalizeArray(arr):

    freq = Counter(arr)

    print(freq.keys(), freq.values())


    max_freq = max(freq.values())

    min_deletions = len(arr) - max_freq
    print(min_deletions)
equalizeArray([3, 3, 2, 1, 3, 2, 5])
