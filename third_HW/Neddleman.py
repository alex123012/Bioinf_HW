def penny(x, y):

    if x == y:
        return 5
    else:
        return -4


def count_score_linear(x, y):
    comand = ('up', 'left', 'dig')

    lenx, leny = len(x) + 1, len(y) + 1
    s = [[(0, 0)] * lenx for _ in range(leny)]

    for i in range(1, lenx):
        s[0][i] = (s[0][i - 1][0] - 10, 0)
    for i in range(1, leny):
        s[i][0] = (s[i - 1][0][0] - 10, 0)

    for i in range(1, leny):
        for j in range(1, lenx):
            isk = [s[i - 1][j][0] - 10,
                   s[i][j - 1][0] - 10,
                   s[i - 1][j - 1][0] + penny(x[j - 1], y[i - 1])]
            d = max(isk)
            dind = comand[isk.index(d)]
            s[i][j] = (d, dind)
    return s


x = input('Enter first sequence: ').upper()
y = input('Enter second sequence: ').upper()
print('Score =', count_score_linear(x, y)[-1][-1][0])