

# def kaprekarNumbers(p, q):
#     # Write your code here
#     splitNumber = []
#     for i in range(p, q+1):
#         square = str(i * i)
#         d = len(str(i))
#         left_part = square[:-d] if square[:-d] else "0"
#         right_part = square[-d:]
#         if int(left_part) + int(right_part) == i:
#             splitNumber.append(i)

def kaprekarNumbers(p, q):
    # Write your code here
    listOfKaprekar = []

    for num in range(p, q+1):
        square = str(num * num)
        d = len(str(num))

        print(d)

        left_part = square[:-d] if square[:-d] else "0"
        right_part = square[-d:]
        print(right_part)

        if int(left_part) + int(right_part) == num:
            listOfKaprekar.append(num)

    # return listOfKaprekar


    print(" ".join(map(str, listOfKaprekar)))







kaprekarNumbers(1, 100)