N, K = map(int, input().split())
out = 0

result = []
people = [i for i in range(1, N+1)]
while people:
    out = (out + K - 1) % len(people)
    temp = people.pop(out)
    result.append(str(temp))
result = ', '.join(result)
print(f'<{result}>')

"""
    1
  7      2
6            3
    5    4        
"""
#     *           2 / 7
# 1 2 3 4 5 6 7   2 + (3 - 1) / 7 -1
#         *       4 / 6
# 1 2 4 5 6 7     4 + (3 - 1) / 6 -1
#   *             1 / 5
# 1 2 4 5 7       1 + (3 - 1) / 5 - 1
#       *         3 / 4
# 1 4 5 7
#     *           2 / 3
# 1 4 5          
# *               0 / 2
# 1 4