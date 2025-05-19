#
#
#
# def group_anagrams(words):
#     anagram = {}
#     for word in words:
#
#         sortedwordKey = ''.join(sorted(word))
#         # print(sortedwordKey)
#         if sortedwordKey in anagram:
#             anagram[sortedwordKey].append(word)
#         else:
#             anagram[sortedwordKey] = [word]
#
#     return anagram.values()
#
#
# words = ["123", "321", "231", "456", "465", "789"]
#
# print(group_anagrams(words))




# def findanagram(words):
#
#     anagram = {}
#
#     for word in words:
#         print(sorted(word))
#         sortedwords = ''.join(sorted(word))
#         print(sortedwords)
#         if sortedwords in anagram:
#             anagram[sortedwords].append(word)
#         else:
#             anagram[sortedwords] = [word]
#
#     print(anagram.values())
#
#
# words = ["123", "321", "231", "456", "465", "789"]
# findanagram(words)





# def IsAnangram(words):
#     srtedword = ''.join(sorted(words[0]))
#     print(srtedword)
#     for i in range(1, len(words)):
#         if ''.join(sorted(words[i])) == srtedword:
#             print(words[i] + " "+ "this is anagram")
#         else:
#             print(words[i] + " " + "this is not anagram")
#
# IsAnangram(["tester", "ertest", "test"])
#
#
#
#
# print(set(["tester", "help", "test", "test"]))
# print(''.join(set("tester")))

#
# testttt= ["tester", "hel1p", "test", "test"]
# testing = list(filter(lambda x: "e" not in sorted(x), testttt))
# print(testing)
#
#
# values = {1: "test", 2: "test2", 3: "test3", 4: None}
#
# filter1 = list(filter(lambda x: x[1] == None, values.items()))
# print(filter1)
#
#
# set(11, 22, 11, 13)
from collections import Counter

def makingAnagrams(s1, s2):
    # Write your code here

    counter1 = Counter(s1)
    counter2 = Counter(s2)

    print(counter1)
    print(counter2)

    total_deletion = 0
    allValues = set(counter2.keys()).union(counter1.keys())
    print(allValues)

    for char in allValues:

        total_deletion += abs(counter1.get(char, 0) - counter2.get(char, 0))

    print(total_deletion)





makingAnagrams("absdjkvuahdakejfnfauhdsaavasdlkj", "djfladfhiawasdkjvalskufhafablsdkashlahdfa")
