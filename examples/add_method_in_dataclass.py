#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt


@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (
            sin((phi_2 - phi_1) / 2) ** 2
            + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2
        )
        return 2 * r * asin(sqrt(h))


def main():

    print("\n=== Пример работы класса Position ===\n")

    oslo = Position("Осло", lon=10.8, lat=59.9)
    vancouver = Position("Ванкувер", lon=-123.1, lat=49.3)
    berlin = Position("Берлин", lon=13.4, lat=52.5)

    print("Города:")
    print(f"  1) {oslo.name}: долгота={oslo.lon}, широта={oslo.lat}")
    print(f"  2) {vancouver.name}: долгота={vancouver.lon}, широта={vancouver.lat}")
    print(f"  3) {berlin.name}: долгота={berlin.lon}, широта={berlin.lat}\n")

    print("Расстояния между городами (в км):")
    dist1 = oslo.distance_to(vancouver)
    print(f"  От {oslo.name} до {vancouver.name}: {dist1:.2f} км")

    dist2 = oslo.distance_to(berlin)
    print(f"  От {oslo.name} до {berlin.name}: {dist2:.2f} км")

    dist3 = berlin.distance_to(vancouver)
    print(f"  От {berlin.name} до {vancouver.name}: {dist3:.2f} км")


if __name__ == "__main__":
    main()
