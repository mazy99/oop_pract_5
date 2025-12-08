#!/usr/bin/env python3
# -*- coding: utf-8 -*


from tasks.product import Product_list


def test_add_and_order_products():
    pl = Product_list()
    pl.add("Банан", 0.8, "Фрукты")
    pl.add("Яблоко", 1.2, "Фрукты")
    pl.add("Морковь", 0.5, "Овощи")

    names = [p.name for p in pl.products]
    assert names == ["Банан", "Морковь", "Яблоко"]

    assert pl.products[0].price == 0.8
    assert pl.products[0].category == "Фрукты"


def test_get_products_by_category_existing():
    pl = Product_list()
    pl.add("Банан", 0.8, "Фрукты")
    pl.add("Яблоко", 1.2, "Фрукты")

    result = pl.get_products_by_category("Фрукты")
    assert "Банан" in result
    assert "Яблоко" in result
    assert "Фрукты" in result


def test_get_products_by_category_nonexistent():
    pl = Product_list()
    pl.add("Морковь", 0.5, "Овощи")

    result = pl.get_products_by_category("Мясо")
    assert result == "В категории 'Мясо' нет продуктов."


def test_str_nonempty_list():
    pl = Product_list()
    pl.add("Банан", 0.8, "Фрукты")

    result = str(pl)
    assert "Банан" in result
    assert "0.8" in result
    assert "Фрукты" in result


def test_str_empty_list():
    pl = Product_list()
    result = str(pl)
    assert "Списко продуктов пуст" in result
    assert "Ошибка" in result
