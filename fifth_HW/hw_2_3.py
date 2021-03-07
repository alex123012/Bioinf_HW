def suffix_arr(x="ATATATTAG"):

    x = x + '$' if '$' not in x else x
    shifts = [x]

    for i in range(1, len(x)):
        shifts.append(x[i:] + x[:i])
    shifts.sort()

    suffix_arr = [len(shift) - shift.index('$') for shift in shifts]
    return shifts, suffix_arr


def BWT(x, suffix=None):
    x = "ATATATTAG" if not x else x
    x += "$"
    if not suffix:
        _, suffix = suffix_arr(x)

    return ''.join([x[i - 2] for i in suffix])


def main():
    x = input('Enter sequence: ').upper()
    l1 = BWT(x)
    print(l1)
    print()
    check(x)


if __name__ == '__main__':
    main()
