


def longest_consecutive(array):

    dict = {}
    ans = 0
    for num in array:
        if len(str(num)) in dict:
            dict[len(str(num))] += 1
        else:
            dict[len(str(num))] = 1

    for key in dict:
        ans = max(ans, dict[key])

    print(ans)










nums = [100, 4, 200, 1, 3, 2, 150, 22, 44, 66, 88, 99, 1111, 2233, 3335, 6666, 2222, 6666, 7777 ]

longest_consecutive(nums)