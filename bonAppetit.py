


def bonAppetit(bill, k, b):
    # Write your code here
    bill[k] = 0
    print(list(bill))
    if sum(bill) // 2 == b:
        print(0)
    else:
        ans = b - (sum(bill) // 2)
        print(ans)


bonAppetit([3, 10, 2, 9], 1, 12)