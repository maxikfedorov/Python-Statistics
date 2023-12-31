import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_csv("insurance.csv")

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].hist(data["age"], bins=60)
axs[0, 0].set_title("Age Distribution")
axs[0, 0].set_xlabel("Age")
axs[0, 0].set_ylabel("Count")

axs[0, 1].hist(data["bmi"], bins=20)
axs[0, 1].set_title("BMI Distribution")
axs[0, 1].set_xlabel("BMI")
axs[0, 1].set_ylabel("Count")

axs[1, 0].hist(data["children"], bins=6)
axs[1, 0].set_title("Children Distribution")
axs[1, 0].set_xlabel("Number of Children")
axs[1, 0].set_ylabel("Count")

axs[1, 1].hist(data["charges"], bins=20)
axs[1, 1].set_title("Charges Distribution")
axs[1, 1].set_xlabel("Charges")
axs[1, 1].set_ylabel("Count")

plt.tight_layout()
plt.show()

# Каждая гистограмма отображает распределение одного из числовых показателей в файле "insurance.csv". Вот что означает каждая гистограмма:

#     Гистограмма возраста (age) показывает, сколько людей в выборке имеют определенный возраст. Например, на гистограмме можно увидеть, что большинство людей в выборке имеют возраст в диапазоне от 20 до 40 лет.
#     Гистограмма индекса массы тела (bmi) показывает, как распределены значения индекса массы тела в выборке. Например, на гистограмме можно увидеть, что большинство людей в выборке имеют индекс массы тела в диапазоне от 25 до 35.
#     Гистограмма числа детей (children) показывает, сколько людей в выборке имеют определенное количество детей. Например, на гистограмме можно увидеть, что большинство людей в выборке не имеют детей.
#     Гистограмма затрат на медицинское обслуживание (charges) показывает, как распределены затраты на медицинское обслуживание в выборке. Например, на гистограмме можно увидеть, что большинство людей в выборке имеют низкие затраты на медицинское обслуживание, но есть небольшое количество людей с очень высокими затратами.
