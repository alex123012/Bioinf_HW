import numpy as np
from scipy.stats import uniform, norm
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rv = uniform(0, 1)
x = rv.rvs(size=100000)
a = []
for i in x:
    a.append(np.cosh(i) + np.sinh(i) + 2 * i)

print((np.mean(a)))

n = 100
p = 0.2

mu = n * p
sigma = np.sqrt(n * p * (1 - p))
rv2 = norm(mu, sigma)

df2 = pd.DataFrame()
df2["x"] = np.linspace(mu - 5 * sigma, mu + 5 * sigma, 1000)
df2["CDF(x)"] = rv2.cdf(df2["x"])
sns.lineplot(data=df2, x="x", y="CDF(x)")
plt.tight_layout()
plt.show()
