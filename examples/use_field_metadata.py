#!/usr/bin/env python3
# -*- coding: utf-8 -*


from dataclasses import dataclass, field


@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={"unit": "degrees"})
    lat: float = field(default=0.0, metadata={"unit": "degrees"})


def main():
    pos = Position("Null Island")
    print(pos)


if __name__ == "__main__":
    main()
