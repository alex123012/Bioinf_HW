from functools import wraps
import matplotlib.pyplot as plt
import unittest as ut
import time


class test_magick(ut.TestCase):
    def test_us(self):
        list_r = [i * 2 for i in range(0, 500)]
        list_l = [i for i in range(0, 1000) if i % 2 != 0]
        check = list(range(0, 1000, 2))

        for i in list_r:
            with self.subTest(case=i):
                self.assertTrue(is_in_logn(i, check)[0])
                self.assertTrue(is_in_n(i, check)[0])
                self.assertTrue(best_func(i, check)[0])
                self.assertTrue(recur_logn(i, check)[0])

        for i in list_l:
            with self.subTest(case=i):
                self.assertFalse(is_in_logn(i, check)[0])
                self.assertFalse(is_in_n(i, check)[0])
                self.assertFalse(best_func(i, check)[0])
                self.assertFalse(recur_logn(i, check)[0])


def check_time(func):

    @wraps(func)
    def wrapped(x, y):

        start = time.time()
        x = func(x, y)
        return x, time.time() - start

    return wrapped


@check_time
def is_in_logn(x, list_x):

    start = 0
    stop = int(len(list_x) - 1)
    search = False

    while start <= stop and not search:

        ind = int((start + stop) // 2)

        if list_x[ind] == x:
            search = True
            break
        elif list_x[ind] > x:
            stop = ind - 1
        else:
            start = ind + 1

    return search


@check_time
def recur_logn(x, list_x):

    ind = len(list_x) // 2

    if list_x[ind] == x:
        return True
    elif len(list_x) < 2:
        return False
    elif list_x[ind] > x:
        return recur_logn(x, list_x[:ind])[0]
    else:
        return recur_logn(x, list_x[ind:])[0]


@check_time
def is_in_n(x, list_x):

    for i in list_x:

        if x == int(i):
            return True

    return False


@check_time
def best_func(x, list_x):

    # Рофлянка
    if x in list_x:
        return True

    else:
        return False


def main():

    list_x = map(float,
                 input('Введите последовательность через пробел: ').split())
    list_x = sorted(list(list_x))
    print(list_x)
    x = float(input("Введите число: "))
    print(is_in_logn(x, list_x)[0])


def test_time():

    func = [is_in_logn, recur_logn, is_in_n, best_func]
    result = []
    for func in func:
        print(func)
        res = []
        for j in range(100, 2000):
            list_r = tuple(range(10)) * (10 * j)
            tmp = [func(333, list_r)[1] for _ in range(20)]
            res.append(sum(tmp) / len(tmp))
        result.append(res)
    return result


def print_fig():
    tmp, x = test_time(), tuple(range(0, 1900))

    y1, y2, y3, y4 = tmp

    fig, ax = plt.subplots(1, 1,
                           figsize=(15, 10),
                           tight_layout=True)

    ax = plt.plot(x, y1, '-',
                  color='black',
                  markersize=1,
                  label='is_in_logn')
    ax = plt.plot(x, y2, '-',
                  color='yellow',
                  markersize=1,
                  label='recur_logn')
    ax = plt.plot(x, y3, '-',
                  color='blue',
                  markersize=1,
                  label='is_in_n')
    ax = plt.plot(x, y4, '-',
                  color='orange',
                  markersize=1,
                  label='best_func')
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == '__main__':
    # print_fig()
    # main()
    ut.main()
