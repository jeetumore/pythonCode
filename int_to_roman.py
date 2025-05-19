#
#
# def integer_to_rom(number):
#     roam_list = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
#
#     symbol_result = ""
#     for symbol, value in reversed(roam_list):
#         if number // value:
#             count = number // value
#             symbol_result += (symbol*count)
#             number = number % value
#
#     print(symbol_result)
#
# integer_to_rom(1994)
#
#
#
#
# def intToRoman(num):
#     num_map = {
#         1: "I",
#         5: "V",    4: "IV",
#         10: "X",   9: "IX",
#         50: "L",   40: "XL",
#         100: "C",  90: "XC",
#         500: "D",  400: "CD",
#         1000: "M", 900: "CM",
#     }
#
#     res = ""
#
#     for n in sorted(num_map, reverse=True):
#         while int(n) <= num:
#             res += num_map[int(n)]
#             num -= int(n)
#
#     print(res)
#
# intToRoman(3749)



# def lengthOfLastWord(s: str):
#     list1 = len(s.split()[-1])
#     print(list1)
#
# lengthOfLastWord("Hello world")
#
#
# prefix = "flower"
# print(prefix[:-2])
#
#

# def convert(s, numRows):
#     if len(s) == 1:
#         return s
#     result=""
#
#     for row in range(numRows):
#         increment= (numRows -1) * 2
#         for i in range(row, len(s), increment):
#             result += s[i]
#             if (row > 0 and row < len(s) -1 and i + increment -2 * row < len(s)):
#                 result += s[i + increment -2 * row]
#
#     print(result)
#
#
# convert("PAYPALISHIRING", 3)


# def reverseWords(s):
#     print(" ".join(s.split()[::-1]))
#
# reverseWords("the sky is blue")
#
#
# def strStr(haystack, needle):
#     # for i in range(len(haystack) - len(needle) + 1):
#     #     if haystack[i:i+len(needle)] == needle:
#     #         return i
#     # return -1
#
#     print(haystack.find(needle))
#
#
# strStr("sadbutsad", "sad")

import re

def isPalindrome(s):
    news = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    reverseNews = news[::-1]
    return True if reverseNews == news else False

print(isPalindrome("A man, a plan, a canal: Panama"))



find