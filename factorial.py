


def factorial(n):
    # Base case: when n is 1, return 1
    if n == 1:
        return 1
    else:
        # Recursive case: n * factorial of n-1
        a = n * factorial(n - 1)
        print(a)
        return a


# Example usage
result = factorial(25)
print(result)  # Output: 120