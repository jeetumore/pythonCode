


def maxProduct(nums):
    array1 = []
    ans = 1

    def generate_subarrays(arr, size):
        array = []
        for i in range(len(arr) -size +1):
            array.append(arr[i:i + size])
        return array

    def multiply(arr):
        product = 1
        for i in arr:
            print(int(i))
            product *= i
        return product

    for j in range(1, len(nums)):
        linklist1 = generate_subarrays(nums, j)
        test = map(lambda x: multiply(x), linklist1)
        print(list(test))
        # ans = max(multiply(generate_subarrays(nums, j)), ans)





        print(ans)

maxProduct([1, 2, 3, 4, 5, 6, 7])