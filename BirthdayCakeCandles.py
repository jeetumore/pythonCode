


def birthdayCakeCandles(candles):
    # Write your code here
    for i in range(len(candles)):
        midValue = i
        for j in range(i+1, len(candles)):
            if candles[j] > candles[midValue]:
                midValue = j

        candles[i], candles[midValue] = candles[midValue], candles[i]

    print(list(candles))
    ans = candles[0:len(candles)].count(candles[0])
    print(ans);


candle=[3, 2, 1, 3]
birthdayCakeCandles(candle)









def birthdayCakeCandles1(array):

    for i in range(len(array)):
        midValue = i
        for j in range(i+1, len(array)):
            if array[j] > array[midValue]:
                midValue = j
        temp = array[i]
        array[i] = array[midValue]
        array[midValue] = temp

    ans = array[0:len(array)].count(array[0])


    print(ans)


candle1=[1, 3, 2, 1, 3, 3]



birthdayCakeCandles1(candle1)









