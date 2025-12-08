#!/usr/bin/env python3
# -*- coding: utf-8 -*


from product import Product_list

if __name__ == "__main__":

    print("=== Создание списка и добавление продуктов ===")
    plist = Product_list()

    plist.add("Хлеб", 45.0, "Еда")
    plist.add("Молоко", 80.5, "Еда")
    plist.add("Шампунь", 250.0, "Быт")
    plist.add("Яблоки", 120.0, "Еда")

    print(plist)
    print()

    print("=== Фильтрация по категории ===")
    print(plist.get_products_by_category("Еда"))
    print()

    print("=== Пустая категория ===")
    print(plist.get_products_by_category("Техника"))
    print()

    print("=== Тест 4: Проверка обработки пустого списка ===")
    empty_list = Product_list()
    print(empty_list)
