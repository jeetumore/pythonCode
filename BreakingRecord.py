
def breakingRecords(scores):
    # Write your code here
    HighestScore = scores[0]
    HighestScoreCount = 0
    lowestScore = scores[0]
    lowestScoreCount = 0
    ArrayInteger = []

    for i in range(1, len(scores)):
        if scores[i] > HighestScore:
            HighestScoreCount += 1
            HighestScore = scores[i]
        elif scores[i] < lowestScore:
            lowestScoreCount += 1
            lowestScore = scores[i]


    ArrayInteger.append(HighestScoreCount)
    ArrayInteger.append(lowestScoreCount)
    print(list(ArrayInteger))

score = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]\

breakingRecords(score)