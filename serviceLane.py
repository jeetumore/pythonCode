#
#
#
# def serviceLane(n, cases, width):
#     # Write your code here
#     array = []
#     for i in cases:
#         print(i)
#         temp = n
#         for j in range(i[0]+1, i[-1]+1):
#             if width[j] <= temp:
#                 temp = width[j]
#                 print(temp)
#
#         array.append(temp)
#
#     print(array)
#
# serviceLane(5, [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]], [1, 2, 2, 2, 1])




def serviceLane(n, cases, width):
    # Write your code here
    results = []
    for start, end in cases:
        results.append(min(width[start:end+1]))
    return results

print(serviceLane(5, [[2, 3], [1, 4], [2, 4], [2, 4], [2, 3]], [1, 2, 2, 2, 1]))