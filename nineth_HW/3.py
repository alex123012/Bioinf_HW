from scipy.stats import uniform


def uniform_rvs_1(a, b):
    return (b - a) * uniform(0, 1).rvs() + a


def uniform_rvs_2(a, b):
    return uniform(a, b).ppf(uniform(0, 1).rvs())


print(uniform_rvs_1(1, 100))
print(uniform_rvs_2(1, 100))
