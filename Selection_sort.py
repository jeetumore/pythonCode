



# def selection_sort(array):
#     n = len(array)
#     for i in range(n):
#         middle_value = i
#         for j in range(i+1, n):
#             if array[i] > array[j]:
#                 middle_value = j
#             array[i], array[middle_value] = array[middle_value], array[i]
#
#     return array
#
#
#
#
# def selection_sorting(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(n -i -1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1],  array[j]
#
#     return array


print(selection_sorting([5, 3, 8, 4, 2]))
# def bubble_sorted(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(n - i - 1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#
#     return array
#
#
# print(bubble_sorted([5, 3, 8, 4, 2]))


# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# print(bubble_sort([5, 3, 8, 4, 2]))


# def insertion_sorted(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         j = i - 1
#         while j >=0 and array[j] > key:
#             array[j+1] = array[j]
#             j -= 1
#         array[j + 1] = key
#         print(array)
#     return array
#
# print(insertion_sorted([5, 3, 8, 4, 2]))



items = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_words = sorted(items, key=lambda x:x[1], reverse=True)
print(sorted_words)  # Output: ['apple', 'banana', 'cherry', 'grape']



list1 = [1, 5, 3]
list2 = [4, 2, 6]

camputing = list(map(lambda x, y : x - y if x > y else x + y, list2, list1))
print(camputing)

list1 = [[1, 2], [5, 6], [3, 4]]
converingtostring= list(map(lambda x: list(map(lambda y:y*2, x)), list1))
print(converingtostring)





