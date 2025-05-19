from collections import deque

# def segment(x, space):
#     Q = deque()          #Initializing a deque
#     n = len(space) #[2, 5, 4, 6, 8] # X = 3
#
#     ans = 0

    # for i in range(0, n):
    #     while len(Q): # remove elements which are out of scope of current window
    #         r = Q.popleft()
    #         if i - (x-1) <= r:
    #             Q.appendleft(r)
    #             break
    #     while len(Q): # maintain monotonicity
    #         r = Q.pop()
    #         if space[r] < space[i]:
    #             Q.append(r)
    #             break
    #     Q.append(i)
    #     if i >= x-1:  # update the final answer
    #         t = Q.popleft()
    #         ans = max(ans, space[t])
    #         Q.appendleft(t)
    # print(ans)

#     Q = deque()          #Initializing a deque
#     n = len(space) #[2, 5, 4, 6, 8] # X = 3



# def diskSpaceAnalysis(x, space):
#     Q = deque()
#     ans = 0
#     n = len(space)
#     for i in range(len(space)):
#         while len(Q):
#             r = Q.popleft()
#             if i - (x - 1) <= r:
#                 Q.appendleft(r)
#                 break
#
#         while len(Q):
#             r = Q.pop()
#             if space[i] > space[r]:
#                 Q.append(r)
#                 break
#
#         Q.append(i)
#         if i >= (x -1):
#             r = Q.popleft()
#             ans = max(ans, space[r])
#             Q.appendleft(r)
#     print(ans)





def diskapceAnalysis(x, space):

    ans = 0
    Q = deque()

    for i in range(len(space)):

        while len(Q):
            r = Q.popleft()
            if i - (x - 1) <= r:
                Q.appendleft(r)
                break

        while len(Q):
            r = Q.pop()
            if space[i] > space[r]:
                Q.append(r)
                break

        Q.append(i)
        if i >= x-1:
            r = Q.popleft()
            ans = max(ans, space[r])
            Q.appendleft(r)

    print(ans)




diskapceAnalysis(3, [2, 5, 4, 6, 8])



















# def segment(x, space):
#     Q = deque()
#     ans = 0
#     lenSpace = len(space)
#
#     for i in range(0, lenSpace):
#
#         while len(Q):
#             r = Q.popleft()
#             if i - (x-1) <= r:
#                 Q.appendleft(r)
#                 break
#
#         while len(Q):
#             r = Q.pop()
#             if space[r] < space[i]:
#                 Q.append(r)
#                 break
#
#         Q.append(i)
#         if i >= x-1:
#             r = Q.popleft()
#             ans = max(ans, space[r])
#             Q.appendleft(r)
#
#     print(ans)












