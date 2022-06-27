A, B = input().split()

print(int(A.replace('6', '5'))+int(B.replace('6', '5')),
      int(A.replace('5','6'))+int(B.replace('5','6')))



# cases_A = [int(A)]
# for i, char in enumerate(A):
#     if char == '5':
#         cases_A.append(int(A[:i] + '6' + A[i+1 :]))
#     if char == '6':
#         cases_A.append(int(A[:i] + '5' + A[i+1 :]))
        
# cases_B = [int(B)]
# for i, char in enumerate(B):
#     if char == '5':
#         cases_B.append(int(B[:i] + '6' + B[i+1 :]))
#     if char == '6':
#         cases_B.append(int(B[:i] + '5' + B[i+1 :]))
        
# cases = []
# hello = []
# for word_A in cases_A:
#     for word_B in cases_B:
#         cases.append(sum([word_A, word_B]))
#         hello.append([word_A, word_B])
        
# print(hello)
# print(min(cases), max(cases))