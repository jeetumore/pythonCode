
#
#
def bigSorting(unsorted):
    #Write your code here
    for i in range(len(unsorted)): #["123", "4", "56", "7890", "12", "345", "678", "90"]
        middleValue = i #123
        for j in range(i, len(unsorted)): #123
            if int(unsorted[j]) < int(unsorted[middleValue]):
                middleValue = j
        unsorted[i], unsorted[middleValue] = unsorted[middleValue], unsorted[i]
    # sorted_number = sorted(unsorted, key=lambda x: (len(x), x))
    return unsorted

unsorted = [-2, 1, 2, 3, 5, -1, 0]

print(bigSorting(unsorted))


#
# def sortingAray(listofnumbers):
#
#     for i in range(len(listofnumbers)):
#         middleValue = i
#         for j in range(i, len(listofnumbers)):
#             if listofnumbers[j] < listofnumbers[middleValue]:
#                 middleValue = j
#         listofnumbers[i], listofnumbers[middleValue] = listofnumbers[middleValue], listofnumbers[i]
#     print(listofnumbers)
#
# sortingAray([123, 4, 56, 7890, 12, 345, 678, 90])
# a = []
# for i in range(ord('a'), ord('z')+5):
#     a.append(i)
# print('\n'.join(list(map(lambda x: chr(x), a))))