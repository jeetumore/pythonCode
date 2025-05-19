


def meanmedian(arr):

    n =len(arr)
    mean = sum(arr) / n

    median = 0
    middle = n // 2
    for i in range(len(ads)):
        if arr[i] == arr[middle]:
            median = arr[middle]
            break

    print(f"Mean : {mean}, Median {median}")



ads = [10, 5, 8, 15, 3]

meanmedian(ads)