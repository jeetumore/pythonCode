
n = 9
requests = ["www.abc.com", "www.abc.com", "www.abc.com", "www.abc.com", "www.abc.com"]


# def rateLimiter(n, requests):
#     ans = []
#     for i in range(0, len(requests)):
#         if requests[ max(0, i -5 + 1)  : i + 1].count(requests[i]) > 2 or requests[max(0, i - 30 + 1) : i + 1].count(requests[i]) > 5:
#             requests[i] = "null"
#             ans.append("Status Error NOT OK")
#         else:
#             ans.append("Status code 200 OK")
#
#     print(ans)




# def rateLimiter(n, requests):
#     ans = []
#     for i in range(0, len(requests)):
#         if requests[max(0, i - 5 + 1) : i + 1].count(requests[i]) > 2 or requests[max(0, i - 30 + 1) : i + 1].count(requests[i]) > 5:
#             requests[i] = "null"
#             ans.append("Error")
#         else:
#             ans.append("OK")
#     print(list(requests))
#     print(ans)



#
# def rateLimiter(n, requests):
#     ans = []
#     for i in range(0, len(requests)):
#         if requests[ max(0, i - 5 + 1): i +1].count(requests[i]) > 2 or requests[max(0, i - 30 + 1): i + 1].count(requests[i]) > 5:
#             requests[i] = "null";
#             print("Error")
#         else:
#             print("status OK")






n = 9
requests = ["www.abc.com", "www.abc.com", "www.abc.com", "www.abc.com", "www.xyz.com"]

def ratelimiter(n, requests):
    res = []
    for i in range(len(requests)):
        if requests[max(0, i - 5 + 1): i + 1].count(requests[i]) > 2:
            requests[i] = "Null"
            print("Error")
        else:
            print("OK")
















ratelimiter(n, requests)