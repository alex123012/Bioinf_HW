from scipy.stats import binom
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def bin_nll(data):
    probs = np.arange(0.01, 1, 0.01)
    x = list(range(max(data), int((data.mean() + 1) * 2 + 10)))
    y = [[np.log(binom.pmf(data, n, p)).sum() for p in probs] for n in x]

    tmp = [max(i) for i in y]
    n = x[tmp.index(max(tmp))]

    tmp = y[tmp.index(max(tmp))]
    p = probs[tmp.index(max(tmp))]
    return n, p, x, y


def main():
    x, y = 15, 0.5
    res_n, res_p = [], []
    # for _ in range(20):
    data = binom.rvs(x, y, size=100)
    n, p, x, y = bin_nll(data)
    res_n.append(n), res_p.append(p)
    print('n =', np.mean(res_n))
    print('p =', np.mean(res_p))

    probs = np.arange(0.01, 1, 0.01)
    df = pd.DataFrame(y, columns=probs, index=x)

    df = df.melt(ignore_index=False)

    sns.set(style = "darkgrid")
    sns.set_palette('Pastel1')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection = '3d')
    x = df.index
    y = df.variable
    z = df.value
    ax.scatter(s=2, xs=x, ys=y, zs=z) #cmap=sns.color_palette('Pastel1', as_cmap=True))

    ax.set_xlabel("n values")
    ax.set_ylabel("p values")
    ax.set_zlabel("NLL")

    plt.show()


if __name__ == '__main__':
    main()
