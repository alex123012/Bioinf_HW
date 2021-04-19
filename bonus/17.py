from scipy.stats import binom
import numpy as np


def bin_nll(data):
    probs = np.arange(0.01, 1, 0.01)
    x = list(range(max(data), int((data.mean() + 1) * 2 + 10)))
    y = [[np.log(binom.pmf(data, n, p)).sum() for p in probs] for n in x]

    tmp = [max(i) for i in y]
    n = x[tmp.index(max(tmp))]

    tmp = y[tmp.index(max(tmp))]
    p = probs[tmp.index(max(tmp))]
    return n, p


def main():
    x, y = 15, 0.5
    res_n, res_p = [], []
    for _ in range(20):
        data = binom.rvs(x, y, size=100)
        n, p = bin_nll(data)
        res_n.append(n), res_p.append(p)
    print('mean n =', np.mean(res_n))
    print('mean p =', np.mean(res_p))


if __name__ == '__main__':
    main()
