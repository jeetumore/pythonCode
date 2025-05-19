
def divisibleSumPairs(n, k, ar):
    # #Write your code here
    # array = sorted(ar)
    # count = 0
    # for i in range(0, n):
    #      for j in range(i+1, n):
    #          if array[i] < array[j] and (array[j] + array[i]) % k == 0:
    #              count += 1
    #
    # print(count)

    count = 0
    for i in range(0, n):
        middleValue = i
        for j in range(i+1, len(ar)):
            if ar[j] < ar[middleValue]:
                middleValue = j
        ar[i], ar[middleValue] = ar[middleValue], ar[i]

    print(ar)
    # for i in range(0, n):
    #     for j in range(i+1, n):
    #         if ar[i] < ar[j] and (ar[j] + ar[i]) % k == 0:
    #             count += 1


    print(count)

n = 6
k = 3
ar = [31415926535897932384626433832795, 1, 3, 10, 3, 5]


divisibleSumPairs(n, k, ar)



# def divisibleSumPairs(n, k, ar):
#     # Write your code here
#     count = 0
#
#     for i in range(len(ar)):
#         for j in range(i+1, n):
#             if (ar[j] + ar[i]) % k == 0:
#                 count += 1
#
#
#     return count