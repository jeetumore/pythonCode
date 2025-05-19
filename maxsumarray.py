





def maxSumSubarray(arr, k):
    sumMax = 0
    for i in range(len(arr)-k):
        print(arr[i:k+i])
        sumMax = max(sum(arr[i:(k+i)]), sumMax)

        print(sumMax)
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
maxSumSubarray(arr, k)




def pringString(s):
    for i in s:
        print(i)

pringString("kjitendra")