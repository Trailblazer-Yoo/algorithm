import sys

input = lambda: sys.stdin.readline()
N = int(input())
# if N == 1:
#     print()
# else:
#     deno = 2
#     while True:
#         N, rema = divmod(N, deno)
#         if N == 0 and rema == 1:
#             break
#         elif rema != 0:
#             N = N * deno + rema
#             deno += 1
#         elif rema == 0:
#             print(deno)
            
deno = 2
while N != 1:
    if N % deno == 0:
        print(deno)
        N /= deno
    else:
        deno += 1