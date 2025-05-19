



def sortword(word):
    n = len(word)
    sortedword = list(sorted(word))
    print(sortedword)
    joinword = ''.join(sortedword)
    print(joinword)
    removedeplicate = set(joinword)
    newline = ''.join(sorted(removedeplicate))
    print(newline)

    filternine = list(filter(lambda x: x != '9', newline))
    print(filternine)




sortword("911213345")