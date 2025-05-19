#
#
# def dayOfProgrammer(year):
#     if year == 1918:
#         return "26.09.1918"
#     elif (year < 1918 and year % 4 == 0) or (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#         return f"12.09.{year}"
#     else:
#         return f"13.09.{year}"
#         # Write your code here
#     days256 = 256
#     totaldaytillAugust = 243
#     if year == 1918:
#         days = totaldaytillAugust - 13
#         day256 = days256 - days
#         print(f"{day256}.09.{year}")
#     elif year < 1918:
#         if year % 4 == 0 or (year % 400 == 0 or year % 100 != 0):
#             day256 = days256 - (totaldaytillAugust + 1)
#             print(print(f"{day256}.09.{year}"))
#
#         else:
#             day256 = (days256 - totaldaytillAugust)
#             print(print(f"{day256}.09.{year}"))
#
#     else:
#         if year > 1918 and year % 4 == 0:
#             print(totaldaytillAugust)
#             day256 = days256 - (totaldaytillAugust + 1)
#             print(f"{day256}.09.{year}")
#         else:
#             day256 = (days256 - totaldaytillAugust)
#             print(f"{day256}.09.{year}")
#
# a = 1800
#
# dayOfProgrammer(a)


def dayOfProgrammer1(year):
    # Write your code here
    if year == 1918:
        print("26.09.1918")
    elif (year < 1918 and year % 4 == 0) or (year % 400 == 0 and year % 100 != 0 ):
        print(f"12.09.{year}")
    else:
        print(f"13.09.{year}")

a = 1801

dayOfProgrammer1(a)