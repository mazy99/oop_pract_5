#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


def main():

    pos = Position("Oslo", 10.8, 59.9)
    print("Город:", pos.name)
    print("Долгота:", pos.lon)
    print("Широта:", pos.lat)

    pos2 = Position("Oslo", 10.8, 59.9)
    print("\nПример 2 (сравнение):", pos == pos2)

    locations = {
        pos: "Столица Норвегии",
        Position("Berlin", 13.4, 52.5): "Столица Германии",
    }
    print("\nПример 3 (использование как ключа словаря):")
    for key, value in locations.items():
        print(f"  {key} -> {value}")

    print("\nПример 4 (неизменяемость):")
    try:
        pos.name = "New Name"
    except Exception as exc:
        print("  Ошибка при попытке изменить объект:", exc)


if __name__ == "__main__":
    main()
