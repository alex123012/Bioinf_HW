def make_sa(word):

    suff = {word[i:]: i for i in range(len(word))}
    return list(suff[suffix]
                for suffix in sorted(suff.keys()))


def bwt_transform(word, sa=None):

    if sa is None:
        sa = make_sa(word)
    return "".join(word[idx - 1] for idx in sa)


def main():
    string = input()
    sa = make_sa(string)
    bwt = bwt_transform(string, sa)
    print(bwt)
    print(sa)


if __name__ == '__main__':
    main()

"""
>>> for i in dictir:
...     print(f'{i}: {dictir[i]}')
...
ORF1ab: 285.0579642068674
E: 652.237885462555
M: 721.4820359281437
ORF10: 237.38793103448276
N: 697.7879269261318
ORF3a: 413.99032648125757
ORF6: 338.92972972972973
ORF7a: 307.6876712328767
ORF7b: 240.12977099236642
S: 194.24522376341272
ORF8: 465.0082191780822
>>> dictir
{'ORF1ab': 285.0579642068674, 'E': 652.237885462555, 'M': 721.4820359281437, 'ORF10': 237.38793103448276, 'N': 697.7879269261318, 'ORF3a': 413.99032648125757, 'ORF6': 338.92972972972973, 'ORF7a': 307.6876712328767, 'ORF7b': 240.12977099236642, 'S': 194.24522376341272, 'ORF8': 465.0082191780822}
"""
