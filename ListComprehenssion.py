
from collections import Counter

from pandas import sortlib

#[expression for item in iterables if condiction ]
#
# nested_list = [[1, 2, [10, 16]], [4, 5, [12, 13] ], [6, 7, 8, 9, [14, 15]]]
#
# result = [item for sublist in nested_list for item in sublist[-1]]
#
# print(result)




# def longestCommonPrefix(strs):
#     """
#     :type strs: List[str]
#     :rtype: str
#     """
#     # minlength = min([len(x) for x in strs])
#     # print(minlength)
#     # stringNew = ""
#
#     if not strs:
#         return ""
#
#     prefix = strs[0]
#     for st in strs[1:]:
#         while not st.endswith(prefix):
#             prefix = prefix[1:]
#             if not prefix:
#                 return ""
#
#     return prefix
#
# print(longestCommonPrefix(["flowerthong","flowthong","flighthong"]))





lst = ["apple", "banana", "apple", "orange", "banana", "apple"]
# count_dict = dict(Counter(lst))
#
# print(count_dict)


dict1 = {}

for i in range(len(lst)):
    if lst[i] in dict1:
        dict1[lst[i]] += 1
    else:
        dict1[lst[i]] = 1


sort = sortlib.read_dict(dict1)
# sort_colum = sortlib.read_csv('input.csv')
sort = sort.sort_values()
# testsorted.to_csv('output8.csv', index=False)




