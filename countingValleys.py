def countingValleys(steps, path):
    altitude = 0
    valleys = 0

    for i in path:
        if i == "U":
            altitude += 1
            if altitude == 0:
                valleys +=1
        else:
            altitude -= 1

    print(valleys)

countingValleys(8, "UDDDUDUUUDDDUDUUDDU")



# /\      /\
#   \    /  \    /
#    \/\/    \/\/