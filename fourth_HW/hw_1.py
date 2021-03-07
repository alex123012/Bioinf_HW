x = list(map(float, input('Enter sequence: ').split()))

if not x:
    x = [1, 2, -10, 9, 1]

S, y = [0] * len(x), [['', '']] * len(x)
S[0], y[0] = x[0], (0, 0)

for i in range(1, len(S)):
    if S[i - 1] + x[i] > x[i]:
        S[i] = S[i - 1] + x[i]
        y[i] = (y[i - 1][0], i)
    else:
        S[i] = x[i]
        y[i] = (i, i)

print(max(S), y[S.index(max(S))])
