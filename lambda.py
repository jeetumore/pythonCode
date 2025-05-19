

# add = lambda x, y: x + y
# print(add(3, 4))  # Output: 7
#
#
# #As arguments to other functions: Lambda functions are commonly used as arguments to higher-order functions like map(), filter(), and sorted().
# points = [(2, 3, 4), (5, 1, 6), (4, 7, 9), (1, 9, 11)]
#
# list1 = sorted(points, key=lambda x: x[0])
# print(list1)

#
#
#
# words = ['apple', 'banana', 'kiwi', 'pear', 'grapefruit']
#
# list2 = sorted(words, key=lambda x: x[1])
# print(list2)


people = [
    {'name': 'John', 'age': 30},
    {'name': 'Doe', 'age': 25},
    {'name': 'Alice', 'age': 35},
    {'name': 'Bob', 'age': 20}
]

test = sorted(people, key=lambda x: x['name'])
print(test)


# words = ['Banana', 'apple', 'Cherry', 'date']
#
# test = lambda x: x + x
# print(test(words[0]))


# numbers = [1, 2, 3, 4, 5]
# # Use map with a lambda function to square each number
#
# squared = tuple(map(lambda x : x * x, numbers))
# print(squared)

# words = ['Banana', 'apple', 'Cherry', 'date']
#
# upperCase = list(map(lambda x: x.istitle(), words))
# print(upperCase)


#
# list1 = [1, 2, 3, 4]
# list2 = [4, 5, 6, 3]
# Use map with lambda to multiply corresponding elements

# duplicate = list(map(lambda x : x if x in list2 else "NONE", list1))
# duplicate1 = list(filter(lambda x : x != "NONE",  duplicate))
# print(duplicate1)

#
# duplicate2 = list(map(lambda x : True if x not in list2 else False , list1))
# print(duplicate2)

#
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 12, 13, 14]
# # First, filter even numbers, then square them using map
# squared_evens = list(filter(lambda x: x % 2 == 0, numbers))
# squared_evens1 = list(map(lambda x : x * x, squared_evens ))
#
# one = list(map(lambda x : x * x, filter(lambda x: x % 2 == 0, numbers)))
# print(one)

# numbers = [34, 2, 23, 67, 1, 89, 21]
# sorted_number = sorted(numbers, key=lambda x : x, reverse=True)
# print(sorted_number)
#
#
# words = ['apple', 'banana', 'kiwi', 'pear', 'strawberry']
# sorted_word = sorted(words, key=lambda x: x, reverse=True )
# print(sorted_word)


# students = [('Alice', 85), ('Bob', 75), ('Charlie', 95), ('Dave', 90)]
# sorted_dict = sorted(students, key=lambda x: x[0])
# print(sorted_dict)

# books = [
#     {'title': 'Harry Potter', 'price': 250},
#     {'title': 'Percy Jackson', 'price': 200},
#     {'title': 'Hobbit', 'price': 300}
# ]
# sorted_dict = sorted(books, key=lambda x: x['title'])
# print(sorted_dict)

# words = ['banana', 'Apple', 'pear', 'Kiwi', 'strawberry']
#
# sort_ignoreing_case = sorted(words, key=lambda x: x.lower())
# print(sort_ignoreing_case)


# dates = [3 + 4j, 1 + 1j, 2 + 2j, 5 + 12j]
# datesort = sorted(dates, key=lambda x : abs(x))
# print(datesort)


# numbers = [1, 2, 3, 4, 5]
# square_element = list(map(lambda x : x * x, numbers ))
# print(square_element)
#
#
# words = ['apple', 'banana', 'cherry']
# upperlistString = list(map(lambda x : x.upper(), words))
# print(upperlistString)
#
#
#
# words = ['elephant', 'tiger', 'lion', 'zebra']
# lenthofeachstring = list(map(lambda x : len(x), words))
# print(lenthofeachstring)
#
# celsius = [0, 20, 30, 36.4, 100]
# covertFarhnight = list(map(lambda x: x * 9/5 + 32, celsius))
# print(covertFarhnight)
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]

# sumlist = list(map(lambda x, y, z : x + y + z, list1, list2, list3  ))
# print(sumlist)
#
#
# measurements = [(70, 150, 11, "a"), (65, 120, 12, "b"), (72, 180, 14, "c")]
#
# convertpound = list(map(lambda x : (x[0] * 2.54, x[1] * 0.453592, x[2], x[3]) , measurements ))
# print(convertpound)

#
# numbers_as_strings = ['1', '2', '3', '4', '5']
# print(list(map(lambda x : int(x), numbers_as_strings)))

#
# numbers = [10, 20, 30]
#
# squarfuction = list(map(lambda x : x ** 2, numbers))
# print(squarfuction)
# havelfuction = list(map(lambda x : x / 2, numbers))
# print(havelfuction)
#
#
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# largestNumber = list(map(lambda x : max(x), list_of_lists))
# print(largestNumber)







