def find_med(x):
    if (len(x) % 2) == 0:
        ind = (len(x) // 2)
        return (x[ind - 1] + x[ind]) / 2

    else:
        return x[len(x) // 2]


def bubble_sort(x):
    n = len(x)
    for i in range(n - 1):
        for j in range(n - i - 1):

            if j < n and x[j] > x[j + 1]:
                x[j], x[j + 1] = x[j + 1], x[j]

    return x


def main():
    a = list(map(float, ('Enter numbers divided by space: ').split()))
    x = bubble_sort(a)
    print(x, find_med(x), sep='\n')


if __name__ == "__main__":
    main()
