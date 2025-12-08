#!/usr/bin/env python3
# -*- coding: utf-8 -*


from storage_package.limited_storage import LimitedStorage

if __name__ == "__main__":

    print("=== Создание с неверной ёмкостью ===")
    try:
        s = LimitedStorage[int](capacity=-3)
    except ValueError as e:
        print("Ошибка при создании:", e)
    print()

    print("=== Переполнение хранилища ===")
    s = LimitedStorage[int](capacity=2)
    try:
        s.add(10)
        s.add(20)
        s.add(30)
    except OverflowError as e:
        print("Ошибка при добавлении:", e)
    print()

    print("=== Корректная работа хранилища ===")
    s = LimitedStorage[int](capacity=3)
    s.add(10)
    s.add(20)
    print("Текущее состояние:", s)
    print("Заполнено?", s.is_full())

    s.add(30)
    print("После добавления третьего элемента — заполнено?", s.is_full())
    print("Итоговое состояние:", s)
