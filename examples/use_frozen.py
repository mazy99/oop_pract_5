#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0


def main():

    pos = Position("Oslo", 10.8, 59.9)
    print(pos.name)
    print(pos.lon)
    print(pos.lat)


if __name__ == "__main__":
    main()
