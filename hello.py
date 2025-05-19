# def addToList(val, lista=[]):
#     lista.append(val)
#     return lista
#
# # list1 = ["1"]
#
# list1 = addToList(1) # ["1"]
# list2 = addToList(123,[]) # ["123"]
# list3 = addToList('a') # ["a"]
# print ("list1 = %s" % list1) # list1 = ["1"]
# print ("list2 = %s" % list2) # list2 = ["123"]
# print ("list3 = %s" % list3) # list3 = ["a"]



# i = 1
# while i <= 10:
#     if i==5:
#         continue
#     print(i)
#     i+=1

# 1 -> 1
# 2 -> 2
# 3 -> 3
# 4 -> 4
# 5


# print("hello, world")
# variable = 1
# print(type(variable))
# print(id(variable))
# #help()
# dir(variable)
#
# list1 = [1, 2, 3, 4, 5]
# list1.insert(0, 5)
# list1.remove(5)
# list1.remove(5)
# print(list1)

# class Parent:
#     def show(self):
#         print("Parent class")
#
# class Child(Parent):
#     def show(self):
#         print("child")
#         super().show()
#
# obj = Child()
# obj.show()


def event_number(n):
    num = 0
    while num < n:
        yield num
        num += 2
        print(num)

even = event_number(10)
print(tuple(even))


# def my_gen():
#     print("Start")
#     yield 1
#     print("Between yields")
#     yield 2
#     print("End")
#     yield 3
#     print("End")
#
#
# g = my_gen()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))