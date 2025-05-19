


def findduplicate(array):

    map1 = {}

    for i in array:
        if i in map1:
            map1[i] += 1
        else:
            map1[i] = 1

    for key, value in map1.items():
        if value > 1:
            print(key)

array = [1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 1]

findduplicate(array)