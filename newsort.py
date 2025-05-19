


# def sortword(word):
#     char_list = list(word)
#     for i in range(len(char_list)):
#         for j in range(0, len(char_list)-i -1):
#             if char_list[j] > char_list[j + 1]:
#                 char_list[j], char_list[j+1] = char_list[j+1], char_list[j]
#
#
#     print(''.join(list(char_list)))
#
#
# sortword("911213345")


def sortnumber(word):

    charlist = list(word)
    for i in range(len(charlist)):
        temp =  charlist[i]
        for j in range(len(charlist)):
            if charlist[j] > temp:
                charlist[i], charlist[j] = charlist[j], charlist[i]
                temp = charlist[j]


    print(charlist)




    print(''.join(list(charlist)))


sortnumber("933871221651143214")
sort
