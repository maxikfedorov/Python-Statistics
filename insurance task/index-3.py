from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("insurance.csv")

import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

sns.boxplot(x=data["age"], ax=axs[0, 0])
axs[0, 0].set_title("Age Distribution")

sns.boxplot(x=data["bmi"], ax=axs[0, 1])
axs[0, 1].set_title("BMI Distribution")

sns.boxplot(x=data["children"], ax=axs[1, 0])
axs[1, 0].set_title("Children Distribution")

sns.boxplot(x=data["charges"], ax=axs[1, 1])
axs[1, 1].set_title("Charges Distribution")

plt.tight_layout()
plt.show()

# Из box-plot можно сделать следующие выводы:

#     Распределение возраста (age) имеет медиану около 40 лет и интерквартильный размах от 27 до 54 лет. Также на графике есть несколько выбросов, что говорит о том, что в выборке есть люди с очень высоким возрастом.
#     Распределение индекса массы тела (bmi) имеет медиану около 30 и интерквартильный размах от 26 до 35. На графике также есть несколько выбросов, что говорит о том, что в выборке есть люди с очень высоким индексом массы тела.
#     Распределение числа детей (children) имеет медиану около 1 и интерквартильный размах от 0 до 2. На графике нет выбросов, что говорит о том, что в выборке нет людей с очень большим количеством детей.
#     Распределение затрат на медицинское обслуживание (charges) имеет медиану около 9400 долларов и интерквартильный размах от 4740 до 16640 долларов. На графике есть много выбросов, что говорит о том, что в выборке есть люди с очень высокими затратами на медицинское обслуживание.
