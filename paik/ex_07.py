N = [1,2,3,4,0,2]

# def answer(N):
#     result = ["READY","LUCKY"]
#     g_halfN = 0
#     l_halfN = 0
#     for i, _ in enumerate(N):
#         if len(N)/2 <= i:
#             l_halfN += N[i]
#         else:
#             g_halfN += N[i]
#     return result[l_halfN == g_halfN]
def answer(N):
    result = ["READY","LUCKY"]
    return result[sum(N[:int(len(N)/2)]) == sum(N[int(len(N)/2):])]

print(answer(N))