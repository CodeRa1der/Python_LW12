#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import timeit
from functools import lru_cache
import matplotlib.pyplot as plt

# Итеративная версия факториала
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Рекурсивная версия факториала с кэшированием
@lru_cache(maxsize=None)
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Итеративная версия чисел Фибоначчи
def fib_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Рекурсивная версия чисел Фибоначчи с кэшированием
@lru_cache(maxsize=None)
def fib_recursive(n):
    if n <= 1:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

# Функция для оценки скорости выполнения функций
def evaluate_speed(func, *args):
    return timeit.timeit(lambda: func(*args), number=10000)

if __name__ == '__main__':
    # Списки для хранения данных о скорости выполнения функций
    factorial_iterative_times = []
    factorial_recursive_times = []
    fib_iterative_times = []
    fib_recursive_times = []

    # Вычисление времени выполнения функций для различных значений
    for n in range(1, 11):
        factorial_iterative_times.append(evaluate_speed(factorial_iterative, n))
        factorial_recursive_times.append(evaluate_speed(factorial_recursive, n))
        fib_iterative_times.append(evaluate_speed(fib_iterative, n))
        fib_recursive_times.append(evaluate_speed(fib_recursive, n))

    # Построение графиков
    plt.figure(figsize=(10, 6))

    # График для факториала
    plt.subplot(2, 1, 1)
    plt.plot(range(1, 11), factorial_iterative_times, label='Итеративная')
    plt.plot(range(1, 11), factorial_recursive_times, label='Рекурсивная с кэшированием')
    plt.xlabel('Число')
    plt.ylabel('Время (в секундах)')
    plt.title('Факториальная функция')
    plt.legend()

    # График для чисел Фибоначчи
    plt.subplot(2, 1, 2)
    plt.plot(range(1, 11), fib_iterative_times, label='Итеративная')
    plt.plot(range(1, 11), fib_recursive_times, label='Рекурсивная с кэшированием')
    plt.xlabel('Число')
    plt.ylabel('Время в секундах')
    plt.title('Функция Фибоначчи')
    plt.legend()

    plt.tight_layout()
    plt.show()