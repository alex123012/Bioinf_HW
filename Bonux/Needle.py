def penny(x, y, comp={}):

    if x == y:
        return 5
    # if x in comp and comp[x] == y:
    #     return -1
    else:
        return -4


def count_score_linear(x, y):
    comand = ('up', 'left', 'dig')
    comp = {'A': 'G',
            'T': 'C',
            'G': 'A',
            'C': 'T',
            }
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
                   s[i - 1][j - 1][0] + penny(x[j - 1], y[i - 1], comp)]
            d = max(isk)
            dind = comand[isk.index(d)]
            s[i][j] = (d, dind)
    return s


def count_score_aff(x, y):
    comand = ('up', 'left', 'dig')
    comp = {'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G',
            }

    lenx, leny = len(x) + 1, len(y) + 1
    s = [[(0, 0)] * lenx for _ in range(leny)]
    a = [[0] * (lenx) for _ in range(leny)]
    b = [[0] * (lenx) for _ in range(leny)]

    for i in range(1, lenx):
        s[0][i] = (-10 - 0.5 * (i - 1), 0)
        a[1][i] = s[0][i][0] - 10
    for i in range(1, leny):
        s[i][0] = (-10 - 0.5 * (i - 1), 0)
        b[i][1] = s[i][0][0] - 10

    for i in range(1, leny):
        for j in range(1, lenx):
            isk = [a[i][j], b[i][j],
                   s[i - 1][j - 1][0] + penny(x[j - 1],
                                              y[i - 1],
                                              comp)]
            d = max(isk)
            dind = comand[isk.index(d)]
            s[i][j] = (d, dind)
            try:
                a[i + 1][j] = max(s[i][j][0] - 10, a[i][j] - 0.5)
            except IndexError:
                pass
            try:
                b[i][j + 1] = max(s[i][j][0] - 10, b[i][j] - 0.5)
            except IndexError:
                pass
    return s


def print_align(i, j, upper, lower, mid, s, x, y):
    if i == 0 and j == 0:
        return upper[::-1], lower[::-1], mid[::-1]

    ind = s[i][j][1]

    if ind == 'dig':
        upper += x[j - 1]
        lower += y[i - 1]

        mid += '|' if upper[-1] == lower[-1] else '.'

        return print_align(i - 1, j - 1, upper, lower, mid, s, x, y)
    elif ind == 'up':
        upper += '-'
        mid += ' '
        lower += y[i - 1]
        return print_align(i - 1, j, upper, lower, mid, s, x, y)
    elif ind == 'left':
        upper += x[j - 1]
        mid += ' '
        lower += '-'
        return print_align(i, j - 1, upper, lower, mid, s, x, y)
    else:
        if i == 0:
            upper += x[j - 1]
            mid += ' '
            lower += '-'
            return print_align(i, j - 1, upper, lower, mid, s, x, y)
        elif j == 0:
            upper += '-'
            mid += ' '
            lower += y[i - 1]
            return print_align(i - 1, j, upper, lower, mid, s, x, y)


def print_all(s, x, y, all=None):
    if all:
        for i in s:
            print(i)
    res1, res2, mid = print_align(len(s) - 1,
                                  len(s[0]) - 1, '', '', '', s, x, y)

    print()
    print(f"3'- {res1} -5'")
    print(f'    {mid}')
    print(f"5'- {res2} -3'")
    print()
    print('Score:', s[-1][-1][0])


def parse_fasta(name):
    pass


def main():
    x = input('Enter first sequence: ').upper()
    y = input('Enter second sequence: ').upper()
    # s = count_score_aff(x, y)
    # print_all(s, 1)
    s = count_score_linear(x, y)
    print_all(s, x, y)


if __name__ == '__main__':
    main()
