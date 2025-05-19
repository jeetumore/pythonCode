
#
# def superReducedString(s):
#     # Write your code here
#     stack = []
#
#     for i in s:
#         if stack and stack[-1] == i:
#             stack.pop()
#         else:
#             stack.append(i)
#
#     print(stack[-1])





def superReducedString(s):
    # Write your code here
    i = 0
    snew = ""
    while (i <= len(s) -2): #[9-2=7]
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            i = 0
        else:
            i += 1


    print(s)

s = "abba"
superReducedString(s)

def super_reduced_string(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            # Remove the adjacent duplicates
            s = s[:i] + s[i + 2:]
            # Reset the index to check for new adjacent duplicates from the start
            i = 0
        else:
            i += 1

    return s if s else "Empty String"


def super_reduced_string(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the last element if it's the same as the current one
        else:
            stack.append(char)  # Add the current character to the stack

    # Join the stack to form the reduced string
    reduced_string = ''.join(stack)

    return reduced_string if reduced_string else "Empty String"