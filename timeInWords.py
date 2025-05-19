from num2words import num2words


def timeInWords(h, m):

    map = {}

    for i in range(0, 31):
        if i == 15:
            map[i] = "quarter"
        elif i == 30:
            map[i] = "half"
        elif i == 0:
            map[i] = "o'clock"
        else:
            map[i] = num2words(i)

    print(map)

    word = ""
    if h < 12 and h in map:
        if m < 30 and m > 1 and m != 15:
            word = map.get(m) + " minutes past " + map.get(h)
        elif m > 30 and m < 60 and m != 45:
            m = abs(m - 60)
            word = map.get(m) + " minutes to " + map.get(h + 1)
        elif m == 30 or m == 15:
            word = map.get(m) + " past " + map.get(h)
        elif m == 45:
            m = abs(m - 60)
            word = map.get(m) + " to " + map.get(h)
        elif m == 0:
            word = map.get(h) + " " + map.get(m)
        else:
            word = map.get(m) + " minute past " + map.get(h)

    elif h == 12:
        if m < 30 and m > 1 and m != 15:
            word = map.get(m) + " minutes past " + map.get(h)
        elif m > 30 and m < 60 and m != 45:
            m = abs(m - 60)
            word = map.get(m) + " minutes to " + map.get(1)
        elif m == 30 or m == 15:
            word = map.get(m) + " past " + map.get(h)
        elif m == 45:
            word = map.get(m) + " to " + map.get(h)
        elif m == 0:
            word = map.get(h) + " " + map.get(m)
        else:
            word = map.get(m) + " minute past " + map.get(h)


    print(word)



timeInWords(5, 45)