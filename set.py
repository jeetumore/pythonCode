

group1 = {"Alice", "Bob", "Charlie", "jitendra"}
group2 = {"Bob", "David", "Charlie", "ramdas"}


def findDuplicate(group1, group2):
    notduplicateinboth = set(group1) ^ set(group2)
    print(notduplicateinboth)

findDuplicate(group1, group2)


