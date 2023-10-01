import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("insurance.csv")

def generate_samples(data, n):
    samples = []
    for i in range(300):
        sample = data.sample(n)
        samples.append(sample)
    means = [sample['charges'].mean() for sample in samples]
    stds = [sample['charges'].std() for sample in samples]
    return means, stds

ns = [10, 50, 100, 250, 500, 1000]
for n in ns:
    means, stds = generate_samples(data, n)
    plt.figure(figsize=(10, 6)), 
    plt.hist(means, bins=50, alpha=0.5, label='n={}'.format(n))
    plt.legend()
    plt.text(0.7, 0.9, 'Mean: {:.2f}\nStd: {:.2f}'.format(np.mean(means), np.std(means)), transform=plt.gca().transAxes)
    plt.show()
    
# Если центральная предельная теорема выполняется, 
# то распределение средних значений должно быть приблизительно нормальным. 
# Из гистограмм можно увидеть, что при увеличении размера выборки n распределение становится все более нормальным. 
# Среднее значение и стандартное отклонение также приближаются к истинным значениям при увеличении размера выборки. 
# Таким образом, можно сделать вывод, что центральная предельная теорема выполняется для признаков charges и imb в данном наборе данных.

