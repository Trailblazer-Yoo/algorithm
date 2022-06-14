FC, VC, P = map(int, input().split())
print(int(FC / (P - VC))+1 if P - VC > 0 else -1)