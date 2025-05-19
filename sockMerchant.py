


def sockMerchant(n, ar):
    # Write your code here
    pairCount = 0
    for i in range(n):
        for j in range(i+1, n):
            if ar[j] != "null" and ar[j] == ar[i]:
                ar[j] = "null"
                ar[i] = "null"
                pairCount += 1
                break
    print(pairCount)

sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20 ])