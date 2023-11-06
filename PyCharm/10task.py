#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    a = set(input("Введите 1 строку: "))
    b = set(input("Введите 2 строку: "))
    c = a.intersection(b)
    print(f"Общие элементы у первой и второй строк: {c}")