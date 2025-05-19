#
# def TrappingRainWater(arr):
#     n = len(arr) -1
#     maxleft = 0
#     maxright = 0
#     count = 0
#     i  = 0
#     while (i < n):
#         if arr[i] <= arr[n]:
#             if arr[i] > maxleft:
#                 maxleft = arr[i]
#             else:
#                 count += (maxleft - arr[i])
#             i += 1
#         else:
#             if arr[n] > maxright:
#                 maxright = arr[n]
#             else:
#                 count += (maxright -arr[n])
#             n -= 1
#
#     print(count)
#
# arr = [3, 0, 1, 0, 4, 0, 2]
#
# TrappingRainWater(arr)
#
#
#
#
#
# def TrappingRainWater(arr):
#     i  = 0
#     maxleft = 0
#     maxright = 0
#     n = len(arr) -1
#     water = 0
#
#     while (i < n ):
#         if arr[i] <= arr[n]:
#             if arr[i] > maxleft:
#                 maxleft = arr[i]
#             else:
#                 water += maxleft - arr[i]
#             i += 1
#         else:
#             if arr[n] > maxright:
#                 maxright = arr[n]
#             else:
#                 water += maxright - arr[n]
#             n -= 1
#
#     print(water);
#
#
#
#
#
# arr = [3, 0, 1, 0, 4, 0, 2]
#
# TrappingRainWater(arr)










def TrappingRainWater1(arr):
    maxleft = 0
    maxright = 0
    n = len(arr) -1
    i = 0
    water = 0

    while (i < n):
        if arr[i] <= arr[n]:
            if arr[i] > maxleft:
                maxleft = arr[i]
            else:
                water += maxleft - arr[i]
            i += 1
        else:
            if arr[n] > maxright:
                maxright = arr[n]
            else:
                water += maxright - arr[n]
            n -= 1

    print(water)

arr = [0,1,0,2,1,0,1,3,2,1,2,1]

TrappingRainWater1(arr)




def seetower(height):
    n = len(height)
    ans = [0] * n

    def calc(height):
        seetowers = []
        for i in range(n):
            ans[i] += len(seetowers)
            while len(seetowers) >= 0 and height(len(seetowers)) <= height[i]:
                seetowers.pop()
            seetowers.append(i)

    calc(height)




