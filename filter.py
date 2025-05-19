import re

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtereven = list(filter(lambda x : x % 2 == 0, numbers ))
print(filtereven)
#
#
#
#
# words = ['cat', 'elephant', 'dog', 'rabbit', 'ant']
# filterlongerthan3 = list(filter(lambda x : len(x) > 3 , words ))
# print(filterlongerthan3)
#
# numbers = [4, 10, 15, 8, 23, 7, 19]
# filternumber = list(filter(lambda x : x > 10, numbers))
# print(filternumber)
#
# numbers = [-5, 10, -3, 7, 0, -1, 12]
# positiveNumber = list(filter(lambda x : x > 0, numbers))
# print(positiveNumber)
# names = ['Alice', 'Bob', 'Amanda', 'Brian', 'Angela']
# numberstartwithA = list(filter(lambda x : x[0] != "A", names))
# print(numberstartwithA)
#
#
# words = ['apple', 'pear', 'banana', 'grape', 'cherry']
# findemptyString = list(filter(lambda x: len(x) % 2 != 0, words))
# print(findemptyString)


# numbers = [121, 1331, 123, 454, 567, 789, 123454321]
# checkpalindrome = list(filter(lambda x : x == int(str(x)[::-1]), numbers))
# print(checkpalindrome)
# #
# # print(str(numbers[0])[::-1])

# numbers = [2, 4, 7, 10, 13, 16, 19, 20]
# def checkprime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) +1):
#         if i % 2 == 0:
#             return False
#     return True
#
# checkprime = list(filter(lambda x : checkprime(x), numbers ))
# print(checkprime)


people = [('John', 17), ('Alice', 19), ('Bob', 16), ('Emily', 22)]

olderthan18 = sorted(list(filter(lambda x : x[1] , people)), key=lambda x: x[1])
print(olderthan18)

# emails = ['test@gmail.com', 'hello', 'example@domain.com', 'nope@', 'user@site.org']
# email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# emailValidate = list(filter(lambda x : re.match(email_pattern, x), emails))
# print(emailValidate)


