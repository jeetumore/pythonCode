# def findDigits(n):
#     # Write your code here
#     count = 0
#     lenth = len(str(n))
#     print(lenth)
#     Value = n
#     print(Value)
#     while(lenth > 0):
#         temp = Value // 10
#         divisor = Value % 10
#         if divisor > 0 and n % divisor == 0:
#             count += 1
#         Value = temp
#         lenth -= 1
#     print(count)
#
# findDigits(1012)
import re

text = "Hello Python world, welcome to  world Python!"
index = text.split("world")
print(index)  # Output: 6 (index of the first occurrence)


