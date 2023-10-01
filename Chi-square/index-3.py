import pandas as pd

data = pd.DataFrame({
    'Женат': [89, 17, 11, 43, 22, 1],
    'Гражданский брак': [80, 22, 20, 35, 6, 4],
    'Не состоит в отношениях': [35, 44, 35, 6, 8, 22]
})
data.index = ['Полный рабочий день', 'Частичная занятость', 'Временно не работает', 'На домохозяйстве', 'На пенсии', 'Учёба']

from scipy.stats import chi2_contingency

stat, p, dof, expected = chi2_contingency(data)
print("Chi-squared test:")
print("Statistic =", stat, "p-value =", p)

if p < 0.05: 
    print("Нулевая гипотеза отвергается, переменные зависимы.\nСемейное положение влияет на занятость") 
else: 
    print("Нулевая гипотеза не отвергается, переменные независимы.")