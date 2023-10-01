import pandas as pd
import numpy as np

data = pd.read_csv("ECDCCases.csv")

# Проверяем наличие пропущенных значений в данных
missing_values = data.isnull().sum()
total_cells = np.product(data.shape)
total_missing = missing_values.sum()

# Выводим количество пропущенных значений в процентах
print("Total Missing Values:", total_missing)
print("Percentage of Missing Values:", (total_missing / total_cells) * 100, "%")

# # Находим признаки с наибольшим количеством пропущенных значений
# missing_values = data.isnull().sum()
# missing_values = missing_values.sort_values(ascending=False)
# print("Features with the most missing values:")
# print(missing_values.head(2))

# Удаляем два признака, в которых больше всех пропущенных значений
data = data.drop(["Cumulative_number_for_14_days_of_COVID-19_cases_per_100000", "geoId"], axis=1)

# Обрабатываем пропуски для категориальных признаков
data["countriesAndTerritories"] = data["countriesAndTerritories"].fillna(value="other")
data["countryterritoryCode"] = data["countryterritoryCode"].fillna(value="other")
data["continentExp"] = data["continentExp"].fillna(value="other")

# Обрабатываем пропуски для числовых признаков
data["day"] = data["day"].fillna(data["day"].median())
data["month"] = data["month"].fillna(data["month"].median())
data["year"] = data["year"].fillna(data["year"].median())
data["cases"] = data["cases"].fillna(data["cases"].median())
data["deaths"] = data["deaths"].fillna(data["deaths"].median())
data["popData2019"] = data["popData2019"].fillna(data["popData2019"].median())

# Проверяем наличие пропущенных значений в данных после обработки
missing_values = data.isnull().sum()
total_cells = np.product(data.shape)
total_missing = missing_values.sum()

# Выводим количество пропущенных значений в процентах
print("\nNEW Total Missing Values:", total_missing)
print("NEW Percentage of Missing Values:", (total_missing / total_cells) * 100, "%")


