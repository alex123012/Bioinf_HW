def main():
    n = int(input("Введите количество ступенек: "))
    print(count_price(n, formula))


def count_price(n, formula=None):
    if not formula:
        a = [i * 2 + 1 for i in range(1, n + 1)]
    else:
        a = [formula(i) for i in range(1, n + 1)]

    print(a, best_result(a), sep='\n')


def best_result(a):

    for i in len(a):
        pass

    # if len(a) % 2 == 1:
    #     return sum(a[::2])
    # else:
    #     return sum(a[1::2])


def formula(x, a=2, b=4):
    return a * x + b


if __name__ == '__main__':
    main()
