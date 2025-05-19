import os


def squares(a, b):
    # Write your code here
    array = []
    i = 1
    while (i*i <= b):
        if i*i >= a and i*i <= b:
            array.append(i*i)
        i += 1
    return len(array)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
