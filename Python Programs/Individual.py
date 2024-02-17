#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Функция для вычисления факториала
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Функция для вычисления числа сочетаний C^m_n с использованием рекурсии
def combinations(m, n):
    if m == 0 or m == n:
        return 1
    else:
        return combinations(m - 1, n - 1) + combinations(m, n - 1)

# Функция для вычисления числа сочетаний C^m_n с использованием формулы
def combinations_formula(m, n):
    return factorial(n) / (factorial(m) * factorial(n - m))

# Основная часть
if __name__ == '__main__':
    m = int(input('Введите число m: '))
    n = int(input('Введите число n: '))
    if m > n:
        print('Число m не может быть больше числа n')
    else:
        print(f"Число сочетаний C^{m}_{n}, вычисленное с помощью рекурсии:", combinations(m, n))
        print(f"Число сочетаний C^{m}_{n}, вычисленное с помощью формулы:", combinations_formula(m, n))
