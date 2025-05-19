


# def countVisibleTowers(height):
#     n = len(height)
#     ans = [0] * n
#     # print(ans)
#
#     def calc(height):
#         st = []
#         for i in range(n):
#             ans[i] += len(st)
#             while len(st) > 0 and height[st[-1]] <= height[i]:
#                 st.pop()
#             st.append(i)
#
#     calc(height)
#     height.reverse(), ans.reverse()
#     calc(height)
#     ans.reverse()
#
#     print(ans)
#
#
#
# countVisibleTowers([5, 2, 10, 1])

# def countVisibleTowers(height):
#     n = len(height)
#     ans = [0] * n
#
#
#     def calcHeight(height):
#         seeTowers = []
#         for i in range(n):
#             ans[i] += len(seeTowers)
#             while len(seeTowers) > 0 and height[seeTowers[-1]] <= height[i]:
#                 seeTowers.pop()
#             seeTowers.append(i)
#
#     calcHeight(height)
#     height.reverse()
#     ans.reverse()
#     calcHeight(height)
#     ans.reverse()
#
#     return ans





# def countVisibleTower(height):
#
#     n = len(height)
#     ans = n * [0]
#
#     def calc(height):
#         seetower = []
#         for i in range(n):
#             ans[i] += len(seetower)
#             print(seetower)
#             while len(seetower) > 0 and height[seetower[-1]] <= height[i]:
#                 seetower.pop()
#
#             seetower.append(i)
#
#     calc(height)
#     height.reverse()
#     ans.reverse()
#     calc(height)
#     ans.reverse()
#
#     return ans



def seetowers(height):
    n = len(height)
    ans = n * [0]

    def calc(height):
        seetower = []
        for i in range(n):
            ans[i] += len(seetower)
            while len(seetower) > 0 and height[seetower[-1]] <= height[i]:
                seetower.pop()
            seetower.append(i)


    calc(height)
    height.reverse()
    ans.reverse()
    calc(height)
    ans.reverse()

    return ans







print(seetowers([5, 2, 10, 1, 11, 2]))