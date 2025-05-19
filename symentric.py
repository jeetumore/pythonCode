
def addelementtoDict(list1):
    dict = {}

    for i in list1:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict;


def findsymentricsElemenets(list1, list2):

    dict = {}

    for i in list1:
        dict[i] = dict.get(i, 0) + 1

    for i in list2:
        dict[i] = dict.get(i, 0) + 1

    print([key for key, value in dict.items() if value > 1])

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

findsymentricsElemenets(list1, list2)