import os
def diagonalDifference(arr):
# Write your code here
    sum1 = 0
    sum2 = 0
    count = 0
    countR = len(arr)
    for i in range(len(arr)):
        sum1 += arr[i][count]
        sum2 += arr[i][countR]
        count+=1
        countR-=1

    ans = sum1 - sum2
    return abs(ans)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
