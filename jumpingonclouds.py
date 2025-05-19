


def jumpingOnClouds(c, k):
    totalenergy = 100
    n = len(c)
    position = 0

    while True:
        position = (position + k) % n
        print(position)
        totalenergy -= 1

        if c[position] == 1:
            totalenergy -= 2

        if position == 0:
            break

    print(totalenergy)


jumpingOnClouds([0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0], 3)



jumpingOnClouds()