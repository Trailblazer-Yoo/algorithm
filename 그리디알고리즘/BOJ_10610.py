n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))

# N = str(input())
# n = ''.join(sorted(N, reverse = True))

# if '0' not in N:
#     print(-1)
# else:
#     if len(n) > 3:
#         n = n[:n.rfind('0')]
#         nums = sorted(set(n))
#         word_1 = []
#         word_2 = []
#         word_3 = []
#         for i in nums:
#             for j in nums:
#                 if i != j and int(i) + int(j) == 3:
#                     word_1.append((int(i), int(j)))
#                 elif i != j and int(i) + int(j) == 6:
#                     word_2.append((int(i), int(j)))
#                 elif i != j and int(i) + int(j) == 9:
#                     word_3.append((int(i), int(j)))
#         try:
#             word_1 = max(word_1)
#         except:
#             word_1 = (10,10)
#         try:
#             word_2 = max(word_2)
#         except:
#             word_2 = (10,10)
#         try:
#             word_3 = max(word_3)
#         except:
#             word_3 = (10,10)
        
#         m = min(word_1, word_2, word_3)
#         print(m)
#         n = sorted(n, reverse=True)

#         print(''.join(n) + str(m[0]) + str(m[1]) + '0')
        
#     elif len(n) == 3:
#         n = sorted(n)
#         n.remove('0')
#         if int(n[0] + n[1] + '0') % 30 != 0 or int(n[1] + n[0] + '0') % 30 != 0:
#             print(-1)
#         else:
#             print(max(int(n[0] + n[1] + '0'), int(n[1] + n[0] + '0')))
#     elif len(n) == 2:
#         n = sorted(n)
#         n.remove('0')
#         if n[0] == '3' or n[0] == '6' or n[0] == '9':
#             print(int(n[0] + '0'))
#         else:
#             print(-1)
            
            

# 030
# 060
# 090
# 120
# 150
# 180
# 210
# 240
# 270
# 300