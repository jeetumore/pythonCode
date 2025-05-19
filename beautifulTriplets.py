



def beautifulTriplets(d, arr):
    # Write your code here
    map = {}

    for i in range(len(arr)):
        array = []
        temp = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] - temp == d:
                array.append(temp)
                temp = arr[j]

                if len(array) == 3:
                    break
            if len(arr) == j+1:
                array.append(temp)



        # print(array)
        if len(array) == 3:
            map[i] = array
    print(len(map.keys()))






beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10])