

def organizingContainers(containers):
    # Write your code here
    n = len(containers)

    Total_capacity = [sum(container) for container in containers]
    # print(Total_capacity)

    type_total = [sum(containers[i][j] for i in range(n)) for j in range(n)]
    print(list(type_total))
    # type_total = [sum(containers[i]) for i in range(n)]
    # # print(list1)
    # # list2 = [sum(list1[i]) for i in range(n)]
    # # print(list2)



    Total_capacity.sort()
    type_total.sort()

    if Total_capacity == type_total:
        return "Possible"
    else:
        return "Impossible"


print(organizingContainers([[1,2], [2, 1]]))