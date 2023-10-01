import pandas as pd

data = pd.read_csv("bmi.csv")

northwest_bmi = data.loc[data["region"] == "northwest", "bmi"]
southwest_bmi = data.loc[data["region"] == "southwest", "bmi"]

from scipy.stats import shapiro

# Проверяем выборку northwest_bmi на нормальность
stat, p = shapiro(northwest_bmi)
print("\nShapiro-Wilk test for northwest_bmi:")
print("Statistic =", stat, "p-value =", p)

# Проверяем выборку southwest_bmi на нормальность
stat, p = shapiro(southwest_bmi)
print("\nShapiro-Wilk test for southwest_bmi:")
print("Statistic =", stat, "p-value =", p)

from scipy.stats import bartlett

# Проверяем выборки на гомогенность дисперсии
stat, p = bartlett(northwest_bmi, southwest_bmi)
print("\nBartlett test:")
print("Statistic =", stat, "p-value =", p)

from scipy.stats import ttest_ind

# Сравниваем средние значения выборок
stat, p = ttest_ind(northwest_bmi, southwest_bmi)
print("\nT-test:")
print("Statistic =", stat, "p-value =", p)

# Если p-value меньше уровня значимости (обычно 0.05), то нулевая гипотеза отвергается, и можно сделать вывод, что выборки имеют различия. 
# Если p-value больше уровня значимости, то нулевая гипотеза не отвергается, и можно сделать вывод, что выборки не имеют различий. 
# Если выборки не прошли тест на нормальность или гомогенность дисперсии, то результаты t-критерия Стьюдента могут быть неправильными.

# На основе выходных данных можно сделать следующие выводы:

#     Обе выборки прошли тест на нормальность (критерий Шапиро-Уилка), так как p-value значительно больше уровня значимости (0.05).
#     Выборки не прошли тест на гомогенность дисперсии (критерий Бартлетта), так как p-value больше уровня значимости (0.05).
#     Средние значения выборок различаются (t-критерий Стьюдента), так как p-value меньше уровня значимости (0.05).

# Таким образом, можно сделать вывод, что индекс массы тела людей из региона northwest и southwest различается. 
# Однако, из-за того, что выборки не прошли тест на гомогенность дисперсии, результаты t-критерия Стьюдента могут быть неправильными.