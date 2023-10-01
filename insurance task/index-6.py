import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import statsmodels.api as sm

data = pd.read_csv("insurance.csv")

# Проверяем распределение признака bmi на нормальность
bmi = data["bmi"]
bmi_mean = bmi.mean()
bmi_std = bmi.std()

# Вычисляем p-значение для критерия Колмогорова-Смирнова
bmi_ks_stat, bmi_ks_pvalue = st.kstest(bmi, "norm", args=(bmi_mean, bmi_std))
print("KS-test p-value for BMI:", bmi_ks_pvalue)

# Строим график квантилей-квантилей
sm.qqplot(bmi, line="s")
plt.title("Q-Q Plot for BMI")
plt.show()

# Проверяем распределение признака charges на нормальность
charges = data["charges"]
charges_mean = charges.mean()
charges_std = charges.std()

# Вычисляем p-значение для критерия Колмогорова-Смирнова
charges_ks_stat, charges_ks_pvalue = st.kstest(charges, "norm", args=(charges_mean, charges_std))
print("KS-test p-value for Charges:", charges_ks_pvalue)

# Строим график квантилей-квантилей
sm.qqplot(charges, line="s")
plt.title("Q-Q Plot for Charges")
plt.show()

# Из полученных результатов можно сделать следующие выводы:

#     Для признака "bmi" p-значение для критерия Колмогорова-Смирнова равно 0.32, что говорит о том, что распределение признака не отклоняется от нормального распределения на уровне значимости 0.05. Это подтверждается графиком квантилей-квантилей, на котором видно, что распределение признака близко к нормальному распределению.
#     Для признака "charges" p-значение для критерия Колмогорова-Смирнова равно 4.38e-42, что говорит о том, что распределение признака существенно отклоняется от нормального распределения на уровне значимости 0.05. Это подтверждается графиком квантилей-квантилей, на котором видно, что распределение признака значительно отклоняется от нормального распределения.
