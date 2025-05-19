

# def biggerIsGreater(w):
#     # Write your code here
#     string = list(w)
#
#     # for i in range(len(w)):
#     #     for j in range(i, len(w)):
#     #         str = w[j+1:] + w[:j+1]
#     #         if str <= w:
#     #             string.append(str)
#
#     newString = sorted(list(w))
#     print(newString)
#     newString[-1], newString[-2] =  newString[-2] , newString[-1]
#     newString1 = "".join(newString)
#     print(newString1)
#     if newString1 < w:
#         print(newString)
#     else:
#         print("no answer")
# biggerIsGreater("dhck")



def biggerIsGreater(w):

    w = list(w)
    pivot = len(w) - 2


    while pivot >= 0 and w[pivot] >= w[pivot + 1]:
        pivot -= 1

    if pivot == -1:
        return "no answer"

    print(pivot)

    last = len(w) -1
    while w[last] <= w[pivot]:
        print("1")
        last -= 1
    print(last)

    w[pivot], w[last] = w[last], w[pivot]

    w = w[:pivot + 1] + w[pivot + 1:][::-1]

    # Convert the list back to a string
    print( ''.join(w))




biggerIsGreater("abcdfe")