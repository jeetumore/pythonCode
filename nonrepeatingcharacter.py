



def firstNonreapiting(string):
    for i in range(len(string)):
        if string[:len(string)].count(string[i]) == 1:
            print(string[i])
            break

firstNonreapiting("swiss")



def firstNonreapiting(string):
    dict1 = {}

    for char in string:
        if char in dict1:
            dict1[char] += 1
        else:
            dict1[char] = 1

    for char in string:
        if dict1[char] == 1:
            print(char)
            break
    return None

firstNonreapiting("aakbbcc")

