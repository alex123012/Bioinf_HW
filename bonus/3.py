from Needle import penny


def comb(x, y):

    indx = (len(x) + 1) // 2
    lres = forward(x[:indx], y)
    rres = backward(x[indx:], y)

    ls = [i + j for i, j in zip(lres, rres)]
    indy = ls.index(max(ls))

    if len(x) == 1:
        return check_x(x, y)

    if len(y) == 1:
        return check_y(x, y)

    left = comb(x[:indx], y[:indy])
    right = comb(x[indx:], y[indy:])

    return left[0] + right[0], left[1] + right[1], max(ls)


def check_x(x, y):

    if len(y) == 1:
        return x, y

    elif not y:
        return x, '-'

    else:
        if x in y:
            i = y.find(x)
            return len(y[:i]) * '-' + x + len(y[i + 1:]) * '-', y
        return x + '-' * (len(y) - 1), y


def check_y(x, y):

    if not x:
        return '-', y

    else:
        if y in x:
            i = x.find(y)
            return x, len(x[:i]) * '-' + y + len(x[i + 1:]) * '-'
        return x, y + '-' * (len(x) - 1)


def forward(x, y):

    lenx, leny = len(x) + 1, len(y) + 1
    s1 = [-10 * i for i in range(leny)]

    for i in range(lenx - 1):
        s2 = [s1[0] - 10] + [0 for _ in range(leny - 1)]
        for j in range(1, leny):
            isk = [s1[j] - 10,
                   s2[j - 1] - 10,
                   s1[j - 1] + penny(x[i],
                                     y[j - 1])]
            s2[j] = max(isk)
        s1 = s2.copy()
    return s1


def backward(x, y):

    lenx, leny = len(x) + 1, len(y) + 1
    s1 = [-10 * i for i in range(leny - 1, -1, -1)]

    for i in range(lenx - 2, -1, -1):
        s2 = [0 for _ in range(leny - 2, -1, -1)] + [s1[-1] - 10]
        for j in range(leny - 2, -1, -1):
            isk = [s1[j] - 10,
                   s2[j + 1] - 10,
                   s1[j + 1] + penny(x[i], y[j])]
            s2[j] = max(isk)
        s1 = s2.copy()
    return s1


def forward_aff(x, y):

    lenx, leny = len(x) + 1, len(y) + 1
    s1 = [-10 * i for i in range(leny)]
    a1 = [0] + [s1[i] - 10 for i in range(1, leny)]

    for i in range(lenx - 1):
        s2 = [s1[0] - 10] + [0 for _ in range(leny - 1)]
        b1 = [0, s2[0] - 10] + [0 for _ in range(1, leny - 1)]
        for j in range(1, leny):
            a1[j] = max(s1[j] - 10, a1[j - 1] - 0.5)

            isk = [a1[j],
                   b1[j],
                   s1[j - 1] + penny(x[i], y[j - 1])]
            s2[j] = max(isk)

            if j + 1 < leny:
                b1[j + 1] = max(s2[j][0] - 10, b1[j] - 0.5)
        s1 = s2.copy()
    return s1


def main():

    x = input('Enter first sequence: ').upper()
    y = input('Enter second sequence: ').upper()

    if y < x:
        x, y = y, x

    res1, res2, score = comb(x, y)

    mid = ''
    for i, j in enumerate(res1):

        if j == res2[i]:
            mid += '|'
        elif j == '-' or res2[i] == '-':
            mid += ' '
        else:
            mid += '.'

    print()
    print(f"3'- {res1} -5'")
    print(f'    {mid}')
    print(f"5'- {res2} -3'")
    print()
    print('Score:', score)


if __name__ == '__main__':
    main()

# ATGAGTCTCTCTGATAAGGACAAGGCTGCTGTGAAAGCCCTATGG
# CTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAG
