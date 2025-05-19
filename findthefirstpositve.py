

def findmissing(array):

    for i in range(len(array)):
        middleValue = i
        for j in range(i, len(array)):
            if array[j] < array[middleValue]:
                middleValue = j

        array[i], array[middleValue]= array[middleValue], array[i]

    print(array)
    missing = 0
    start = array[0]    
    for i in range(len(array)):
        if array[i] != start:
            missing = array[i] - 1
            break
        start += 1

    print(missing)
array = [1, 9, 7, 8, 5, 4, 2, 3 ]

findmissing(array)