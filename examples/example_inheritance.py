#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class Capital(Position):
    country: str = ""


def main():
    cap1 = Capital("Осло", 10.8, 59.9, "Норвегия")
    cap2 = Capital("Москва", 37.6, 55.8, "Россия")
    cap3 = Capital("Париж", 2.35, 48.85, "Франция")

    pos1 = Position("Эйфелева башня", 2.2945, 48.8584)
    pos2 = Position("Большой каньон", -112.1129, 36.1069)
    pos3 = Position("Стадион Сан-Сиро", 9.2773, 45.4781)

    capitals = [cap1, cap2, cap3]
    positions = [pos1, pos2, pos3]

    print("Столицы:")
    for cap in capitals:
        print(cap)

    print("\nПрочие позиции:")
    for pos in positions:
        print(pos)


if __name__ == "__main__":
    main()
