import pandas as pd

# Загружаем данные из файла data.csv
data = pd.read_csv('data.csv')

# Вычисление средней зарплаты сотрудников
data_salary = data['salary'].mean()


# Список сотрудников, возраст которых больше 30 лет
data_age = data[data['age'] > 30]

print(f"Средняя зарплата сотрудников: {data_salary}")

print('Сотрудники старше 30 лет:')
print(data_age)