def camelcase(s):
    # Write your code here
    countWord = 0
    for i in range(len(s)):
        if s[i].isCap() is False:
            countWord += 1

    return 1 if countWord == 0 else countWord +1








