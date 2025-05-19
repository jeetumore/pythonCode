def migratoryBirds(arr):
    # Write your code here
    my_dict = {}
    for i in arr:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    max_count = 0
    print(my_dict)
    bird_type = float('inf')
    print(bird_type)

    for bird_type_key, count in my_dict.items():
        if count > max_count:
            max_count = count
            bird_type = bird_type_key
        elif count == max_count and bird_type_key > bird_type:
            bird_type = bird_type_key

    print(bird_type)



# def migratoryBirds(arr):
#     # Dictionary to store frequency of each bird type
#     my_dict = {}
#
#     # Count the frequency of each bird type
#     for bird in arr:
#         if bird in my_dict:
#             my_dict[bird] += 1
#         else:
#             my_dict[bird] = 1
#
#     # Initialize variables to track the bird type with the highest frequency
#     max_count = 0
#     min_bird_type = float('inf')  # Start with a large number
#
#     # Iterate through the dictionary to find the bird type with the highest frequency
#     for bird_type, count in my_dict.items():
#         if count > max_count:
#             max_count = count
#             min_bird_type = bird_type
#         elif count == max_count and bird_type < min_bird_type:
#             min_bird_type = bird_type
#
#     return min_bird_type

arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3]
migratoryBirds(arr)


#
# def migratoryBirds(arr):
#     # Dictionary to store frequency of each bird type
#     my_dict = {}
#
#     # Count the frequency of each bird type
#     for bird in arr:
#         if bird in my_dict:
#             my_dict[bird] += 1
#         else:
#             my_dict[bird] = 1
#
#     # Initialize variables to track the bird type with the highest frequency
#     max_count = 0
#     min_bird_type = float('inf')  # Start with a large number
#
#     # Iterate through the dictionary to find the bird type with the highest frequency
#     for bird_type, count in my_dict.items():
#         if count > max_count:
#             max_count = count
#             min_bird_type = bird_type
#         elif count == max_count and bird_type < min_bird_type:
#             min_bird_type = bird_type
#
#     return min_bird_type
