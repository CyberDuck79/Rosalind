# Mendel's First Law

from math import factorial


def couple(n, k):
    return (factorial(n) / factorial(n - k)) / 2


def dominant_probability(k, m, n):
    total_pop = k + m + n
    total_couple = couple(total_pop, 2)
    print(total_couple)
    # all possible k only couple, all k,m couple, all k,n couple, 1/2 for m,n couple, 1/4 m,m couple
    valid_couple = couple(k, 2) + (k * m) + (k * n) + (m * n) * .5 + couple(m, 2) * .75
    return valid_couple/total_couple


print(dominant_probability(29, 19, 19))
