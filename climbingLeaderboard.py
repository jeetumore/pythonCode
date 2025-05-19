#
#
# def climbingLeaderboard(ranked, players):
#     # Write your code here
#     rankedlist = sorted(set(ranked), reverse=True)
#     print(rankedlist)
#     Arr = []
#     index = len(rankedlist) -1
#
#     for score in players:
#
#         while index >= 0 and score >= rankedlist[index]:
#             print(index)
#             index -= 1
#
#         Arr.append(index + 2)
#
#
#
#
#     print(Arr)

def climbingLeaderboard(ranked, players):
    # Write your code here
    rankedlist = sorted(set(ranked), reverse=True)
    print(rankedlist)
    Arr = []
    index = len(rankedlist) -1

    for i in range(len(players)):
        for k in range(index, -1, -1):
            print(k)
            if players[i] >= rankedlist[k]:
                index -= 1
            else:
                break

        Arr.append(index + 2)




    print(Arr)


ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
climbingLeaderboard(ranked, player)