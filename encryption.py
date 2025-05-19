import math
from itertools import zip_longest
# def encryption(s):
    # Write your code here
    # stringwithspace = s.replace(" ", "")
    # print(stringwithspace)
    # n = len(stringwithspace)
    #
    # divisor = int(math.sqrt(n))
    # remainder = n % divisor
    # index = 0
    # list1 = []
    # list2 = []
    # for i in range(n):
    #     if i != 0 and i % divisor == 0 or i == n-1:
    #         list1.append(stringwithspace[index:i])
    #         index = i
    #
    # newlist1 =  [''.join(chars) for chars in zip_longest(*list1, fillvalue='')]

def encryption(s):
    # Remove spaces from the input string
    s = s.replace(" ", "")

    # Determine the grid size
    L = len(s)
    r = math.floor(math.sqrt(L))
    c = math.ceil(math.sqrt(L))
    print(c, r, L)

    # Adjust grid dimensions if necessary
    if r * c < L:
        print("1")
        r += 1

    # Create the grid and populate it with characters
    grid = [s[i:i+c] for i in range(0, L, c)]
    print(grid)

    newlist1 =  [''.join(chars) for chars in zip_longest(*grid, fillvalue='')]
    print(newlist1)



    # index = 0
    # list4 = []
    # for i in range(len(newlist1)):
    #     string = ""
    #     for word in newlist1: 
    #         if index < len(word):
    #             string += word[index]
    #     print(string)
    #     index += 1
    #     list4.append(string)






encryption("have a nice day this is jitendra welcome to my coding session sss")

# input_list = ['haveani', 'cedayth', 'isisjit', 'endrawe', 'lcometo', 'mycodin', 'gsessio', 'nss']
#
# # Using zip with list comprehension to create the desired output
# output = [''.join(chars) for chars in zip(*input_list)]
#
# print(output)