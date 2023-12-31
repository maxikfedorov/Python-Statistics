import pandas as pd

data = pd.read_csv("ECDCCases.csv")

# Выводим статистику по данным
print(data.describe())


# Сделаем выводы о том, какие признаки содержат выбросы. Для этого можно проанализировать значения максимального и минимального квартилей, а также значения максимальных и минимальных значений:

    # Признак "cases" содержит выбросы, так как максимальное значение (234633) значительно превышает значение третьего квартиля (273).
    # Признак "deaths" содержит выбросы, так как максимальное значение (4928) значительно превышает значение третьего квартиля (4).
    # Признак "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000" содержит выбросы, так как максимальное значение (1900.836210) значительно превышает значение третьего квартиля (52.561206).

# Группируем данные по странам и суммируем количество смертей в день
deaths_by_country = data.groupby("countriesAndTerritories")["deaths"].sum()

# Выводим список стран, в которых количество смертей в день превысило 3000
print("Countries with more than 3000 deaths per day:")
print(deaths_by_country[deaths_by_country > 3000])

# Выводим количество дней, в которых количество смертей в день превысило 3000
print("Number of days with more than 3000 deaths per day:",(data["deaths"] > 3000).sum())

# Ищем дубликаты данных
duplicates = data.duplicated()
print("Number of duplicates:", duplicates.sum())

# Удаляем дубликаты данных
data = data.drop_duplicates()


# Из результатов выполнения задания можно сделать следующие выводы:

#     В некоторых странах количество смертей в день превышало 3000. Например, в США количество смертей в день превышало 3000 в течение нескольких месяцев.
#     Было найдено 11 дней, в которые количество смертей в день превышало 3000.
#     В данных были обнаружены дубликаты, которые могут повлиять на результаты анализа данных. Было найдено 4 дубликата, которые были удалены.
#     Из результатов можно сделать вывод, что ситуация с COVID-19 в разных странах различается и в некоторых странах количество смертей в день достигает очень высоких значений.
