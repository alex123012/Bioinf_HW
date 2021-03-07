def C(x=None, ls=('$', 'A', 'C', 'G', 'T')):
    x = "ATATATTAG" if not x else x
    x += "$"
    dictir = {i: sum([x.count(j) for j in ls[:ls.index(i)]]) for i in ls}
    return dictir


def BWT(x, suffix):
    x = "ATATATTAG" if not x else x
    x += "$"

    return ''.join([x[i - 2] for i in suffix])


def suffix_arr(x="ATATATTAG"):

    x = x + '$' if '$' not in x else x
    shifts = [x]

    for i in range(1, len(x)):
        shifts.append(x[i:] + x[:i])
    shifts.sort()

    suffix_arr = [len(shift) - shift.index('$') for shift in shifts]
    return shifts, suffix_arr


def main():
    x = 'ATATATTAG'
    S = [10, 8, 1, 3, 5, 9, 7, 2, 4, 6]
    print(C())
    print(BWT(x, S))


if __name__ == '__main__':
    main()
