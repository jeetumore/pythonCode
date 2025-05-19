

#
# def fiboonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return  1
#     else:
#         return fiboonacci(n-1) + fiboonacci(n-2)
# print(fiboonacci(19))
#
#
#
#
#
#
# def fibbonacciValue(value):
#     prev1 = 0
#     prev2 = 1
#
#     list1 = []
#     list1.append(prev1)
#     list1.append(prev2)
#
#     for i in range(value -1):
#         newFibbonaci = prev1 + prev2
#         list1.append(newFibbonaci)
#         prev1 = prev2
#         prev2 = newFibbonaci
#
#     print(list(list1))
#
# fibbonacciValue(19)



#
# def merge(nums1, m, nums2, n):
#     # merged = []
#     merged = [0]* (m+n)
#     # print(merged)
#     for i in range(m):
#         merged[i] = nums1[i]
#
#     for j in range(n):
#         merged[m+j] = nums2[j]
#
#     print(sorted(merged))
#
# merge([1,2,3],3, [2, 4, 5], 3 )



# def removeDuplicates(nums):
#     index = 0
#     Temp = 0
#     for i in range(len(nums)):
#         if nums[i] != nums[i -1]:
#             nums[index] = nums[i]
#             index += 1
#
#
#
#
#
#     print(nums)


def removeDuplicates(nums):
    # # [1,1,1,2,2,3]
    # right = 1
    # for i in range(len(nums)):
    #     if nums[i] == nums[i - 1]:
    #         nums[right] = nums[i]
    #         right + 1
    #     elif nums[i] != nums[i - 1]:
    #         nums[right] = nums[i - 1]
    #         i + 1

    # return right + 1
    # array = []
    # for i in range(len(nums)):
    #     if nums[i] in array and array.count(nums[i]) > 1:
    #         continue
    #     else:
    #         array.append(nums[i])
    #
    # print(array)

    left = 0
    right = 0

    while right < len(nums):
        count = 1
        while right < len(nums) and nums[right] == nums[right +1]:
            right += 1
            count += 1

        for i in range(min(2, count)):
            nums[left] = nums[right]
            left += 1

        right += 1

    return left



removeDuplicates([0, 0, 0, 1,1,1,2,2,3,3,4,4,4])





