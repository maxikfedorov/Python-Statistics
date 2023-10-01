import numpy as np

observed = np.array([97, 98, 109, 95, 97, 104])

n = observed.sum()
k = len(observed)
expected = np.array([n / k] * k)

from scipy.stats import chisquare

stat, p = chisquare(observed, expected)
print("Хи-квадрат тест:") 
print("Статистика =", stat, "p-значение =", p)

if p < 0.05:
    print("Нулевая гипотеза отвергается, распределение не является равномерным.")
else:
    print("Нулевая гипотеза не отвергается, распределение равномерное.")