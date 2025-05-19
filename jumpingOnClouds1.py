



def jumpingOnClouds(arr):
    position = 0
    n = len(arr)
    i =0

    while (i < len(arr) - 1):
        if i + 2 < len(arr) and arr[i + 2] == 0:
            i += 2
        else:
            i += 1

        position += 1
    return position





arr = [0, 0, 0, 0, 1, 0]

jumpingOnClouds(arr)