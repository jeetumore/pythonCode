

# from collections import Counter

def top_n_frequent_elements(nums: list, n: int) -> list:
    # Step 1: Count frequency of each element using a dictionary
    dict1 = {}
    for i in nums:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    test = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    for key, value in test[:2]:
        print(key)
    print([key for key, value in test[:n]])


    



    # Step 2: Sort the dictionary by frequency (values) in descending order
    # and extract the top N elements (keys)
    # return [key for key, _ in freq_dict.most_common(4)]

nums = [1, 3, 1, 3, 2, 1, 4, 2, 2, 3, 4, 4, 4]
n = 2
print(top_n_frequent_elements(nums, n))  # Output: [4, 1]