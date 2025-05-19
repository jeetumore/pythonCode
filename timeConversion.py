# def timeConversion(s):
#     hour = int(s[:2])
#     suffix = s[-2:]
#
#     if suffix == "AM":
#         if hour == 12:
#             hour = 0
#     else:
#         if hour != 12:
#             hour += 12
#
#     print(f"{hour:02d}{s[2:-2]}")


# def timeConversion(s):
#     # Write your code here
#     AMSuffix = "AM"
#     PMSuffix = "PM"
#     # print(len(s))
#     # suffix = s[0: len(s) - 2]
#     # print(suffix)
#     if s[len(s) - 2:] == AMSuffix:
#         if (s[0:2]) == "12":
#             computestring = str(int(s[0:2]) - 12)
#             if len(computestring) < 1:
#                 newString = "0" + computestring + s[2:len(s) -2]
#             else:
#                 newString = "0" + computestring + s[2:len(s) -2]
#
#             print(newString)
#         else:
#             newstring = s[0: len(s) - 2]
#             print(newstring)
#     elif s[len(s) - 2:] == PMSuffix:
#         if (s[0:2]) < "12":
#             newString = str(int(s[0:2]) + 12) + s[2:len(s) -2]
#             print(newString)
#         elif (s[0:2]) >= "12":
#             newString = str(int(s[0:2])) + s[2:len(s) -2]
#             print(newString)




def timeConversion(s):
    suffix = s[-2:]
    hour = int(s[:2])

    if suffix == "AM":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12

    test = "timein 12 hours format {:02d}{}".format(hour, s[2:-2])
    print(test)

timeConversion("00:45:54AM")