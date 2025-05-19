

def circularArrayRotation(a, k, queries):
    # Write your code here

    for i in range(k):
        temp = a[-1]
        temp1 = a[:-1]
        a = [temp] + temp1


    for q in queries:
        print(a[q])

circularArrayRotation([1, 2, 3], 1, [0, 1, 2])