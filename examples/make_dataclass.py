#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import make_dataclass

Position = make_dataclass(
    "Position",
    [
        ("name", str),
        ("lat", float),
        ("lon", float),
    ],
)


def main():

    moscow = Position("Moscow", 55.7558, 37.6176)
    print("Пример 1:", moscow)

    moscow.lat = 55.75
    print("Пример 2 (изменение lat):", moscow)

    cities = [
        Position("Paris", 48.8566, 2.3522),
        Position("Tokyo", 35.6895, 139.6917),
        Position("New York", 40.7128, -74.0060),
    ]

    print("\nПример 3 (список точек):")
    for city in cities:
        print(" •", city)

    sorted_cities = sorted(cities, key=lambda c: c.name)
    print("\nПример 4 (сортировка по имени):")
    for city in sorted_cities:
        print(" •", city)


if __name__ == "__main__":
    main()
