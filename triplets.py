

# def threeSum(nums):
#     arrNums= []
#     # print(sum(nums))
#     if len(nums) < 4:
#         return arrNums if sum(nums) != 0 else (arrNums.append(nums) or arrNums)
#     for i in range(len(nums)):
#         print(i)
#         arr = [nums[i]]
#         for j in range(len(nums)):
#             if len(arr) < 3:
#                 arr.append(nums[j])
#             else:
#                 if arr not in arrNums and sum(arr) == 0:
#                     arrNums.append(arr)
#                 else:
#                     arr = [nums[i]]
#     print(arrNums)
#
# print(threeSum([-1,0,1,0]))



def threeSum(nums):
    set1 = set()

    sortArr = sorted(nums)
    # print(sortArr)
    # print(arrNums)
    for i in range(len(sortArr) -2):
        left = i+1
        right = len(sortArr)-1
        while left < right:
            sum = sortArr[i] + sortArr[left] + sortArr[right]
            if sum == 0:
                list1 = (sortArr[i], sortArr[left], sortArr[right])  # Convert to tuple
                set1.add(list1)
                left +=1
                right -=1
            elif sum < 0:
                left +=1
            else:
                right -= 1


    print([list(t) for t in set1])







print(threeSum([-1,0,1,0]))