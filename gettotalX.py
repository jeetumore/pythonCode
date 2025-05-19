# #
#
# def getTotalX(a, b):
#     facfirstelm = []
#     facsecondelm = []
#     count = 0
#     joinarray = a + b
#     # print(list(joinarray))
#     sen = len(joinarray) - 1
#     for i in range(0, len(joinarray)):
#         if joinarray[i] % a[0] == 0:
#             facfirstelm.append(joinarray[i])
#             # print(list(facfirstelm))
#         if sen > 1 and joinarray[i] % joinarray[1] == 0:
#             facsecondelm.append(joinarray[(i+1)])
#             # print(list(facsecondelm))
#             # print(sen)
#             sen -= 1
#
#
#     # print(list(facfirstelm))
#     # print(list(facsecondelm))
#     for i in facfirstelm:
#         if i in facsecondelm:
#             count += 1
#     print(count)
#
# a = [2, 4]
# b = [16, 32, 96]
# getTotalX(a, b)





#
# def getTotalX(a, b):
#     def is_factor_of_all(x, arr):
#         # Check if x is a factor of all elements in arr
#         for num in arr:
#             if num % x != 0:
#                 return False
#         return True
#
#     def all_factors_of(x, arr):
#         # Check if x is a multiple of all elements in arr
#         for num in arr:
#             if x % num != 0:
#                 return False
#         return True
#
#     count = 0
#     # We only need to check numbers between max(a) and min(b)
#     for x in range(max(a), min(b)+1):
#         # print(range(max(a), min(b))
#         if all_factors_of(x, a) and is_factor_of_all(x, b):
#             count += 1
#
#     print(count)
#
#
# a = [2, 4]
# b = [16, 32, 96]
# #
# getTotalX(a, b)

def getTotalX(a, b):
    def is_factor_of_all(x, array):
        for number in array:
            if number % x != 0:
                print("false")
                return False
        print("true")
        return True

    def all_factors_of_all(x, array):
        for number in array:
            if x % number != 0:

                return False

        return True


    count = 0
    for x in range(max(a), min(b)+1):
        if all_factors_of_all(x, a) and is_factor_of_all(x, b):
            count += 1

    print(count)


a = [2, 4]
b = [16, 32, 96]
#
getTotalX(a, b)