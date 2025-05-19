import os

def utopianTree(n):

    # Write your code here
    if n <= 0:
        return 1
    Height = 1
    i = 1
    while (i <= n):
        if i % 2 != 0:
            Height += Height
        else:
            Height += 1
        i += 1

    return Height



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
