


def cutTheSticks(arr):
    # Write your code here
    n = len(arr)
    numStrictCut = []
    stickCutCount = 0

    print(sum(arr))
    while sum(arr) > 0:
        minValue = findmin(arr)
        print(minValue)

        for i in range(n):
            if arr[i] > 0:
                arr[i] = arr[i] - minValue
                stickCutCount += 1
        numStrictCut.append(stickCutCount)
        stickCutCount = 0
        print(arr)

    print(numStrictCut)

def findmin(array):
    ans = float('inf')
    for i in range(len(array)):
        if array[i] != 0:
            ans = min(array[i], ans)
    return int(ans)

cutTheSticks([5, 4, 4, 2, 2, 8])