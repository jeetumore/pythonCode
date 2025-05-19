



def merge2dict(dict1, dict2):
    newDict = dict2.copy()

    for key, value in dict1.items():
        if key in dict2:
            newDict[key] += value
        else:
            newDict[key] = value

    print(newDict)


def merge2dict(dict1, dict2):

    test ={ key: dict1.get(key, 0) + dict2.get(key, 0) for key in dict2.keys() | dict1.keys() }
    print(list(dict2.values()))
    test1 = list(dict2.values()) + list(dict1.values())
    print(test1)



dict1 = {'a': 2, 'b': 3, 'c': 8}
dict2 = {'a': 2, 'b': 3, 'c': 8}

merge2dict(dict1, dict2)



