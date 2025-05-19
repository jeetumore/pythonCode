#
#
#
# def print_lowercase_alphabet(h):
#     map = {}
#     i = 0
#     for letter in range(ord('a'), ord('z') + 1):
#         map[chr(letter)] = h[i]
#         i += 1
#     return map
#     #print(dict(map))
#
# # print_lowercase_alphabet(h)
#
# def designerPdfViewer(h, word):
#     # Write your code here
#     Tall = 0
#
#     height = print_lowercase_alphabet(h)
#     print(height)
#     for i in word:
#         if height.get(i) >= Tall:
#             Tall = height.get(i)
#
#     print(Tall * len(word))
# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ,5, 5, 5, 7]
#
# word = "jitendra"
# designerPdfViewer(h, word)


def print_lowercase_alphabet():
    map = {}
    i = 0
    for letter in range(ord('a'), ord('z') + 1):
        print(chr(letter), end=",")

print_lowercase_alphabet()