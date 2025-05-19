


def maxSubArray(nums):
    max_sum = nums[0]
    max_global = nums[0]

    for i in range(1, len(nums)):
        max_sum = max(nums[i], max_sum + nums[i])
        max_global = max(max_sum, max_global)

    print(max_global)




maxSubArray([-1, 2, 3, -4, 5, -1, 2])



