import numpy as np
import pandas as pd

## Рабочие формулы
# Выборочное среднее результатов измерений
def sr(i, j):
    if A[i, 0] % 3 == 1:
        E = 0
        for n in range(i, i+2 + 1):
            E += A[n, j]
        return E/3

    if A[i, 0] % 3 == 2:
        E = 0
        for n in range(i-1, i+1 + 1):
            E += A[n, j]
        return E/3
    
    if A[i, 0] % 3 == 0:
        E = 0
        for n in range(i-2, i + 1):
            E += A[n, j]
        return E/3    
    
# Выборочное среднеквадратичное отклонение
def s(i, j):
    # Выборочное среднее результатов измерений
    if A[i, 0] % 3 == 1:
        E = 0
        for n in range(i, i+2 + 1):
            E += A[n, j]
        sr = E/3

    if A[i, 0] % 3 == 2:
        E = 0
        for n in range(i-1, i+1 + 1):
            E += A[n, j]
        sr = E/3
    
    if A[i, 0] % 3 == 0:
        E = 0
        for n in range(i-2, i + 1):
            E += A[n, j]
        sr = E/3
    
    # Выборочное среднеквадратичное отклонение
    if A[i, 0] % 3 == 1:
        E = 0
        for n in range(i, i+2 + 1):
            E += np.square(A[n, j] - sr)
        return np.sqrt(E/2)

    if A[i, 0] % 3 == 2:
        E = 0
        for n in range(i-1, i+1 + 1):
            E += np.square(A[n, j] - sr)
        return np.sqrt(E/2)
    
    if A[i, 0] % 3 == 0:
        E = 0
        for n in range(i-2, i + 1):
            E += np.square(A[n, j] - sr)
        return np.sqrt(0.5*E/2)

# Cреднеквадратичное отклонение
def sko(i, j):
    # Выборочное среднее результатов измерений
    if A[i, 0] % 3 == 1:
        E = 0
        for n in range(i, i+2 + 1):
            E += A[n, j]
        sr = E/3

    if A[i, 0] % 3 == 2:
        E = 0
        for n in range(i-1, i+1 + 1):
            E += A[n, j]
        sr = E/3
    
    if A[i, 0] % 3 == 0:
        E = 0
        for n in range(i-2, i + 1):
            E += A[n, j]
        sr = E/3
    
    # Выборочное среднеквадратичное отклонение
    if A[i, 0] % 3 == 1:
        E = 0
        for n in range(i, i+2 + 1):
            E += np.square(A[n, j] - sr)
        s = np.sqrt(E/2)

    if A[i, 0] % 3 == 2:
        E = 0
        for n in range(i-1, i+1 + 1):
            E += np.square(A[n, j] - sr)
        s = np.sqrt(E/2)
    
    if A[i, 0] % 3 == 0:
        E = 0
        for n in range(i-2, i + 1):
            E += np.square(A[n, j] - sr)
        s = np.sqrt(E/2)
    
    # Cреднеквадратичное отклонение
    return 2.48 * s

# Количество строк
row = 3

# Количество столбцов
column = 7

# Объявление таблицы
A = np.zeros((row + 1, column + 1))
for i in range(1, row + 1):
    A[i, 0] = i
for j in range(1, column + 1):
    A[0, j] = j

# 1. Координата уровня воды в левой трубке после накачивания воздуха, мм
A[1: , 1:1 + 1] = [
    [5],
    [6],
    [7]
]

# 2. Координата уровня воды в правой трубке после накачивания воздуха, мм
A[1: , 2:2 + 1] = [
    [6],
    [7],
    [8]
]

# 3. Координата уровня воды в левой трубке после выпускания воздуха, мм
A[1: , 3:3 + 1] = [
    [5],
    [6],
    [7]
]

# 4. Координата уровня воды в правой трубке после выпускания воздуха, мм
A[1: , 4:4 + 1] = [
    [5],
    [6],
    [10]
]

# 5. Экспериментальное значение показателя адиабаты
A[1: , 5:5 + 1] = (A[1: , 2:2 + 1] - A[1: , 1:1 + 1]) / ((A[1: , 2:2 + 1] - A[1: , 1:1 + 1]) - (A[1: , 4:4 + 1] - A[1: , 3:3 + 1]))

# 6. СКО показателя адибаты
for i in range(1, 3 + 1):
    j = 5
    A[i, 6] = sko(i, j)

# 7. Теоретическое значение показателя адиабаты
A[1: , 7:7 + 1] = 7/5

# Вывод таблицы
df_A = pd.DataFrame(A)
df_A = df_A.drop(index=[0])
df_A = df_A.drop(columns=[0])
rounded_df_A = df_A.round(decimals=1)
print(rounded_df_A)