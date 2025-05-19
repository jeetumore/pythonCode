
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    AppleCount = 0
    OrangeCount = 0
    for i in apples:
        if (i + a) >= s and (i + a) <= t:
            AppleCount += 1

    for j in oranges:
        if (j + b) >= s and (j + b) <= t:
            OrangeCount += 1

    print(f"{AppleCount}")
    print(f"{OrangeCount}")

countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])





