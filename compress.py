from itertools import groupby
#string S
S = input("Enter the string value:")
for c, X in groupby(S):
    print(f"({len(list(X))}, {c})", end=' ')