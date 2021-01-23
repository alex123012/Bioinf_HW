import unittest as ut
import time


class test_magick(ut.TestCase):
    def test_us(self):
        list_r = list(range(0, 100))
        for i in list_r:
            with self.subTest(case=i):
                self.assertEqual(magick(i), i)


def magick(x=None, start=0, stop=100):

    yes = ['да', 'д', 'yes', 'y', 'ye']

    while (stop >= start):

        current_state = (start + stop) // 2

        if x is None:
            ans = input(f'Верно ли, что загаданное число меньше {current_state}?').lower()
            if ans in yes:
                stop = current_state - 1
            else:
                start = current_state + 1

        elif current_state > x:
            stop = current_state - 1
        else:
            start = current_state + 1
    return stop


def main():
    x = float(input('Введите число: '))
    print('ваше число:', magick())
    print('\n\n')


def test():
    start = time.time()
    magick(123123123123, 0, 10e100)
    print(time.time() - start, '\n')

    start = time.time()
    magick(123123123123, 0, 10e250)
    print(time.time() - start, '\n')

    start = time.time()
    magick(123123123123, 0, 10e500)
    print(time.time() - start, '\n')

    ut.main()


if __name__ == '__main__':
    main()
    # test()
