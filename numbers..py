


# def uniqfile(file):
#     nums =[]
#     with open('out.csv', mode='r') as file:
#         num = [line for line in file.readlines()]
#         print(num)
#
#
#     print(list(set(nums)))
#     print(len(set(nums)))
#
#
# uniqfile('out.csv')



def distributeTheIntheBucket(filepath, M):

    bucket = [[] for _ in range(M)]

    with open(filepath, 'r') as file:
        for index, lines in enumerate(file):
            bucket[ index % M ].append(lines.strip())


    return bucket


filepath = 'inputs.csv'
M = 3

buckets = distributeTheIntheBucket(filepath, M)

for i, bucket in enumerate(buckets):
    print(f"Bucket {i+1}:")
    print("\n".join(bucket))
    print("-" * 20)




