

# def reverse(n):
#     print(int(str(n)[::-1]))
#
# reverse(210)



def beautifulDays(i, j, k):
    # Write your code here
    BeautifulDay = 0
    for i in range(i, j+1):
        if abs(i - (int(str(i)[::-1]))) % k == 0:
            BeautifulDay += 1

    print(BeautifulDay)

beautifulDays(13, 45, 3)

